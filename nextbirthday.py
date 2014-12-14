from creds import *
from datetime import date
from dateutil.relativedelta import relativedelta

def dateWithoutYear(dateToStrip):
    return date(year=date.today().year, month=dateToStrip.month, day=dateToStrip.day)

def daysUntilBirthday(member):
    daysUntil = (dateWithoutYear(member.birthdate()) - date.today()).days
    if daysUntil <= 0:
        daysUntil = 99999999999999999999999
    return daysUntil

def next_birthday():
    activeMembers = ldap.search(active=1)
    birthdayMembers = [member for member in activeMembers if member.birthday]

    if birthdayMembers:
        nextBirthday = min(birthdayMembers, key=daysUntilBirthday)
        return {
            "member": nextBirthday.cn,
            "birthday": nextBirthday.birthdate().isoformat(),
            "age": nextBirthday.age() + 1
        }
    return None

if __name__ == "__main__":
    bday = next_birthday()
    if bday:
        print(bday["member"] + ": " + bday["birthday"])
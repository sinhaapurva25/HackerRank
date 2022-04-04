def fun(s):
    username = s.split("@")[0]
    websitename = s.split("@")[1].split(".")[0]
    websitename = s.split("@")[1].split(".")[1]
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)
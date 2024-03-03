class main:
    def email(emails):
        a = []
        for email in emails:
            addr = email.split("@")
            domain = addr[1]
            localName = addr[0]

            pos = localName.find('+')
            if pos != -1:
                localName = localName[:pos]
            arr = localName.split(".")
            finalName = "".join(arr)

            newEmail = finalName+"@"+domain
            if newEmail not in a:
                a.append(newEmail)
                print(newEmail)
        return len(a)
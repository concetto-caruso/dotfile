#!/usr/bin/env python

import imaplib
import credential

obj = imaplib.IMAP4_SSL('imap.gmail.com')
obj.login(credential.login, credential.password)
obj.select()


print (len(obj.search(None, 'UnSeen')[1][0].split()))

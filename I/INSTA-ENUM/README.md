### INSTA-ENUM
**One-line Description:** 
A versatile Instagram enumeration tool that retrieves user details efficiently, offering persistence even when usernames change, valuable for OSINT investigations.

**Usefulness:** This tool simplifies Instagram profile enumeration for OSINT by swiftly obtaining user information, and its ability to preserve user IDs makes it effective in scenarios where usernames are altered.


### USAGE :


```
┌──(p4ul㉿Root)
└─$ python3 App.py -r -u cristiano
UserName : cristiano
Full Name : Cristiano Ronaldo
BIO : Join my NFT journey on @Binance. Click the link below to get started.
ID (User ID) : 173560420
PIC URL : https://instagram.fsxv1-1.fna.fbcdn.net/v/t51.2885-19/278931269_360124899498969_9006978846103417088_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fsxv1-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=0PxMFp3CGjQAX8hkebz&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfAXlvorUJCc3sgqyhaQJ0gRUAWmmG6OpDyi4Z-KGVR5zQ&oe=653B088E&_nc_sid=8b3546
PIC URL HD : https://instagram.fsxv1-1.fna.fbcdn.net/v/t51.2885-19/278931269_360124899498969_9006978846103417088_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fsxv1-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=0PxMFp3CGjQAX8hkebz&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfC-rVyrMy-Evogmzh7-3S58YihVeMzULqgndWrc6FCmgg&oe=653B088E&_nc_sid=8b3546
UserName : cristiano
FB ID : 17841401692602711
Count of Followers : 609030519
Count of Following : 567
Post Count : 3570
```


### RETRIEVAL USING ID :


```
┌──(p4ul㉿Root)
└─$ python3 App.py -d -i 173560420                                                                                                                      2 ⨯
UserName : cristiano
Full Name : Cristiano Ronaldo
BIO : Join my NFT journey on @Binance. Click the link below to get started.
ID (User ID) : 173560420
PIC URL : https://instagram.fsxv1-1.fna.fbcdn.net/v/t51.2885-19/278931269_360124899498969_9006978846103417088_n.jpg?stp=dst-jpg_s150x150&_nc_ht=instagram.fsxv1-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=0PxMFp3CGjQAX8hkebz&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfAXlvorUJCc3sgqyhaQJ0gRUAWmmG6OpDyi4Z-KGVR5zQ&oe=653B088E&_nc_sid=8b3546
PIC URL HD : https://instagram.fsxv1-1.fna.fbcdn.net/v/t51.2885-19/278931269_360124899498969_9006978846103417088_n.jpg?stp=dst-jpg_s320x320&_nc_ht=instagram.fsxv1-1.fna.fbcdn.net&_nc_cat=1&_nc_ohc=0PxMFp3CGjQAX8hkebz&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfC-rVyrMy-Evogmzh7-3S58YihVeMzULqgndWrc6FCmgg&oe=653B088E&_nc_sid=8b3546
UserName : cristiano
FB ID : 17841401692602711
Count of Followers : 609030734
Count of Following : 567
Post Count : 3570

```
### Practical Application:

1. Acquiring the target's Instagram username and subsequently extracting their user ID, which can be stored for future reference.

2. Conducting a command-line interface (CLI) enumeration of Instagram profiles, making it a straightforward and efficient process.

3. Boasting user-friendliness in its design, ensuring a hassle-free experience.

4. Maintaining its utility even when the Instagram username undergoes modifications, as the user ID remains constant, thus ensuring its effectiveness in such scenarios.

### Suitable Usage Scenarios:

> This tool proves valuable when engaged in the enumeration of Instagram accounts for open-source intelligence (OSINT) purposes.

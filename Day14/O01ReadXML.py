
import xml.dom.minidom

DOMTree = xml.dom.minidom.parse("stud.xml")
collection = DOMTree.documentElement

std = collection.getElementsByTagName('stud')

for st in std:
    print("Student".center(40, "-"))

    if st.hasAttribute('name'):
        print("Student Name :", st.getAttribute('name'))

        dob = st.getElementsByTagName('dob')[0]
        print("DOB :", dob.childNodes[0].data)

        cls = st.getElementsByTagName('class')[0]
        print("CLASS :", cls.childNodes[0].data)

        gen = st.getElementsByTagName('gender')[0]
        print("GENDER :", gen.childNodes[0].data)

        con = st.getElementsByTagName('contact')[0]
        print("CONTACT NO. :", con.childNodes[0].data)

        rtyp = st.getElementsByTagName('rettype')[0]
        print("RETURN_TYPE :", rtyp.childNodes[0].data)



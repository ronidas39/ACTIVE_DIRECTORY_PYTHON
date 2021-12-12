import io
import pyad.adquery
import validate_cn
import pyad.aduser
import pyad.adcontainer
import sys
with io.open("records.csv","r",encoding="utf-8")as f1:
    data=f1.read()
    f1.close()
ou=pyad.adcontainer.ADContainer.from_dn("OU=test,DC=totaltechnology,DC=com")
file_row=data.split("\n")
for row in file_row[1:]:
    attributes=row.split(",")
    employeeID=attributes[0]
    title=attributes[1]
    givenName=attributes[2].strip()
    sn=attributes[3].strip()
    base_sAMAccountName=givenName+sn
    counter=0
    final_cn=validate_cn.gen_cn(base_sAMAccountName,counter)
    if (final_cn==0):
        cn=base_sAMAccountName.strip()
    else:
        cn=base_sAMAccountName+str(final_cn)
        cn=cn.strip()
    print(cn,final_cn)
    mail=cn+"@totaltechnology.com"
    department=attributes[4]
    mobile=attributes[5]
    co=attributes[6]
    l=attributes[7]
    print(ou)
    optional={"givenName":givenName,"sn":sn,"mail":mail,"employeeID":employeeID,"department":department,"mobile":mobile,"co":co,"l":l}
    try: 
        pyad.aduser.ADUser.create(cn,ou,password=None,upn_suffix="totaltechnology.com",enable=False,optional_attributes=optional)
        print(f"user created {employeeID}")

    except Exception as e:
        print(str(e)+f"error occured for {employeeID}")
        sys.exit()

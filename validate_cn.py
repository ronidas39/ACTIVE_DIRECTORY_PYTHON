import pyad.adquery
q=pyad.adquery.ADQuery()

def gen_cn(gn,counter):

    if counter==0:
        cn=gn
    else:
        cn=gn+str(counter)
  
    q.execute_query(
        attributes=["cn"],
        where_clause="sAMAccountName='{}'".format(cn),
        base_dn="DC=totaltechnology,DC=com"
    )
    if(q.get_row_count()>=1):
        counter=counter+1
        return gen_cn(gn,counter)
    
    return (counter)
counter=0
x=gen_cn("AleksandraStone",counter)
print(x)



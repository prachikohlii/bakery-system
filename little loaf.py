import pandas as pd
import mysql.connector as co

sqlco=co.connect(host="localhost",user="root",passwd="12346",database="bakery")
cu=sqlco.cursor()

if sqlco.is_connected():
    print("WELCOME TO 'Little loaf Bakehouse'.........GREAT TASTE IN EVERY BITE")



print("EXPERIENCE THE BEST OF BAKING WITH US. WE SERVE FRESH EVERYDAY. \nWE BAKE,WITH LOVE,ESPECIALLY FOR YOU SO THAT \nYOU FALL IN LOVE AT 'FIRST BITE'")



cu.execute("create table customer(name char(100),gender char(2),address varchar(100),contact nvarchar(20),date varchar(200),cust_order varchar(200),amount int(100),delivery char(30))")
sqlco.commit()




cu.execute("create table bak(iname char(30),icode varchar(30),iprice int(40),availability int(30))")
sqlco.commit()
a=("insert into bak values(%s,%s,%s,%s)")
a1=("mumbai_club_sandwich","d11",50,50)
cu.execute(a,a1)
sqlco.commit()
b=("insert into bak values(%s,%s,%s,%s)")
b1=("grilled_sandwich","d12",35,28)
cu.execute(b,b1)
sqlco.commit()
c=("insert into bak values(%s,%s,%s,%s)")
c1=("chicken_sandwich","d13",40,20)
cu.execute(c,c1)
sqlco.commit()
d=("insert into bak values(%s,%s,%s,%s)")
d1=("tandoori_paneer_sandwich","d14",35,8)
cu.execute(d,d1)
sqlco.commit()
e=("insert into bak values(%s,%s,%s,%s)")
e1=("mushroom_&_cheese_sandwich","d15",40,30)
cu.execute(e,e1)
sqlco.commit()
f=("insert into bak values(%s,%s,%s,%s)")
f1=("patty","d21",20,48)
cu.execute(f,f1)
sqlco.commit()
g=("insert into bak values(%s,%s,%s,%s)")
g1=("mini_pizza","d22",40,37)
cu.execute(g,g1)
sqlco.commit()
h=("insert into bak values(%s,%s,%s,%s)")
h1=("veggie_burger","d23",50,57)
cu.execute(h,h1)
sqlco.commit()
i=("insert into bak values(%s,%s,%s,%s)")
i1=("italian_slice","d24",45,10)
cu.execute(i,i1)
sqlco.commit()
j=("insert into bak values(%s,%s,%s,%s)")
j1=("kulcha","d25",30,60)
cu.execute(j,j1)
sqlco.commit()
k=("insert into bak values(%s,%s,%s,%s)")
k1=("chesse_chilly_foot_long","d26",55,70)
cu.execute(k,k1)
sqlco.commit()
l=("insert into bak values(%s,%s,%s,%s)")
l1=("bread","d31",20,60)
cu.execute(l,l1)
sqlco.commit()
m=("insert into bak values(%s,%s,%s,%s)")
m1=("bun","d32",15,56)
cu.execute(m,m1)
sqlco.commit()
n=("insert into bak values(%s,%s,%s,%s)")
n1=("muffin","d33",15,36)
cu.execute(n,n1)
sqlco.commit()
o=("insert into bak values(%s,%s,%s,%s)")
o1=("brownie","d34",15,45)
cu.execute(o,o1)
sqlco.commit()
p=("insert into bak values(%s,%s,%s,%s)")
p1=("cream_roll","d35",20,67)
cu.execute(p,p1)
sqlco.commit()
q=("insert into bak values(%s,%s,%s,%s)")
q1=("donut","d36",30,90)
cu.execute(q,q1)
sqlco.commit()
r=("insert into bak values(%s,%s,%s,%s)")
r1=("black_forest","d41",45,50)
cu.execute(r,r1)
sqlco.commit()
s=("insert into bak values(%s,%s,%s,%s)")
s1=("pineapple","d42",40,80)
cu.execute(s,s1)
sqlco.commit()
t=("insert into bak values(%s,%s,%s,%s)")
t1=("wonder_chocolate","d43",80,59)
cu.execute(t,t1)
sqlco.commit()
u=("insert into bak values(%s,%s,%s,%s)")
u1=("fruit_nut","d44",70,77)
cu.execute(u,u1)
sqlco.commit()
v=("insert into bak values(%s,%s,%s,%s)")
v1=("celebration","d45",100,49)
cu.execute(v,v1)
sqlco.commit()
w=("insert into bak values(%s,%s,%s,%s)")
w1=("dairy_milk_fruit_&_nut","d51",45,59)
cu.execute(w,w1)
sqlco.commit()
y=("insert into bak values(%s,%s,%s,%s)")
y1=("dairy_milk_crackle","d52",45,112)
cu.execute(y,y1)
sqlco.commit()
z=("insert into bak values(%s,%s,%s,%s)")
z1=("dairy_milk_silk_oreo","d53",70,49)
cu.execute(z,z1)
sqlco.commit()
A=("insert into bak values(%s,%s,%s,%s)")
A1=("dairy_milk_roast_almond","d54",40,40)
cu.execute(A,A1)
sqlco.commit()
B=("insert into bak values(%s,%s,%s,%s)")
B1=("cadbury_five_star_threeD","d55",45,50)
cu.execute(B,B1)
sqlco.commit()
C=("insert into bak values(%s,%s,%s,%s)")
C1=("cadbury_dark_milk","d56",200,100)
cu.execute(C,C1)
sqlco.commit()
D=("insert into bak values(%s,%s,%s,%s)")
D1=("lays_cream_&_onion","d61",20,62)
cu.execute(D,D1)
sqlco.commit()
E=("insert into bak values(%s,%s,%s,%s)")
E1=("lays_tomato_tango","d62",20,69)
cu.execute(E,E1)
sqlco.commit()
F=("insert into bak values(%s,%s,%s,%s)")
F1=("lays_chile_limon","d63",20,57)
cu.execute(F,F1)
sqlco.commit()
G=("insert into bak values(%s,%s,%s,%s)")
G1=("kurkure_masala_munch","d64",20,45)
cu.execute(G,G1)
sqlco.commit()
H=("insert into bak values(%s,%s,%s,%s)")
H1=("kurkure_green_chutney","d65",20,41)
cu.execute(H,H1)
sqlco.commit()
I=("insert into bak values(%s,%s,%s,%s)")
I1= ("bingo_tedhe_medhe","d66",10,30)
cu.execute(I,I1)
sqlco.commit()



cu.execute("create table des(item char(200),description varchar(500))")
sqlco.commit()
J=("insert into des values(%s,%s)")
J1=("mumbai_club_sandwich","2_layered_veggie_club_sandwich")
cu.execute(J,J1)
sqlco.commit()
K=("insert into des values(%s,%s)")
K1=("grilled_sandwich","single_layer_potato_grilled_with_jalapeno_sauce")
cu.execute(K,K1)
sqlco.commit()
L=("insert into des values(%s,%s)")
L1=("chicken_sandwich","heavy_non_veg_with_italian_sauce")
cu.execute(L,L1)
sqlco.commit()
M=("insert into des values(%s,%s)")
M1=("tandoori_paneer_sandwich","processed_cheese_filled_with_tandoori_sauce")
cu.execute(M,M1)
sqlco.commit()
N=("insert into des values(%s,%s)")
N1=("mushroom_&_cheese_sandwich","loaded_with_mushrooms_&_cheese_touched")
cu.execute(N,N1)
sqlco.commit()
O=("insert into des values(%s,%s)")
O1=("patty","potato_filled_crispy_patties")
cu.execute(O,O1)
sqlco.commit()
P=("insert into des values(%s,%s)")
P1=("mini_pizza","olives_loaded_pan_pizza_slice")
cu.execute(P,P1)
sqlco.commit()
Q=("insert into des values(%s,%s)")
Q1=("veggie_burger","veg_loaded_soft_buns_burger")
cu.execute(Q,Q1)
sqlco.commit()
R=("insert into des values(%s,%s)")
R1=("italian_slice","crispy_single_layered_slice_inspired_from_italy")
cu.execute(R,R1)
sqlco.commit()
S=("insert into des values(%s,%s)")
S1=("kulcha","potato_kulcha")
cu.execute(S,S1)
sqlco.commit()
T=("insert into des values(%s,%s)")
T1=("cheese_chilly_foot_long","italian_sauce_filled_hot_dog_slice_with_cheese")
cu.execute(T,T1)
sqlco.commit()
U=("insert into des values(%s,%s)")
U1=("black_forest","chocolate_layered_strawberry_jam_centre_filled")
cu.execute(U,U1)
sqlco.commit()
V=("insert into des values(%s,%s)")
V1=("pineapple","pineapple_pieces_topped_with_white_creamy_layer")
cu.execute(V,V1)
sqlco.commit()
X=("insert into des values(%s,%s)")
X1=("wonder_chocolate","loaded_with_imported_dark_chocolate")
cu.execute(X,X1)
sqlco.commit()
Y=("insert into des values(%s,%s)")
Y1=("fruit_nut","nut_loaded_crunchy_layers")
cu.execute(Y,Y1)
sqlco.commit()
Z=("insert into des values(%s,%s)")
Z1=("celebration","strawberry_jam_3_layered_large_pastry")
cu.execute(Z,Z1)
sqlco.commit()

    
    

def options():
    print("CHOOSE YOUR ACTION")
    print("1=SANDWICHES MENU")
    print("2=SNACKS MENU")
    print("3=PASTRIES MENU")
    print("4=CHOCOLATES MENU")
    print("5=OTHERS MENU")
    print("6=CHIPS MENU")
    print("7=COMBOS")
    print("8=ITEMS' DESCRIPTION MENU")
    print("9=MY CART")
    print("10=DONE ORDERING")

    
def sandwich():
    df=pd.read_sql("select * from bak where icode in('d11','d12','d13','d14','d15')",sqlco)
    print(df)
def snacks():
    df=pd.read_sql("select * from bak where icode in('d21','d22','d23','d24','d25','d26')",sqlco)
    print(df)
def pastries():
    df=pd.read_sql("select * from bak where icode in('d41','d42','d43','d44','d45')",sqlco)
    print(df)
def chocolates():
    df=pd.read_sql("select * from bak where icode in('d51','d52','d53','d54','d55','d56')",sqlco)
    print(df)
def others():
    df=pd.read_sql("select * from bak where icode in('d31','d32','d33','d34','d35','d36')",sqlco)
    print(df)  
def combos():
    print("1: BUY 2 GRILLED SANDWICHES AND GET 1 PINEAPPLE PASTRY FOR FREE")
    print("2: BUY 3 MINI PIZZAS AND GET 1 ITALIAN SLICE FOR FREE")
    print("3: BUY 2 MUMBAI CLUB SANDWICHES AT JUST RS.80")
def chips():
    df=pd.read_sql("select * from bak where icode in('d61','d62','d63','d64','d65','d66')",sqlco)
    print(df)
def des():
    df=pd.read_sql("select * from des",sqlco)
    print(df)
def deli():
    print("HOW WOULD YOU LIKE YOUR ORDER TO BE DELIVERED:")
    print("1=EAT IN")
    print("2=TAKEAWAY")
    print("3=GET HOME DELIVERED")
   
        









def entry():
    print("KINDLY MAKE YOUR ENTRY BEFORE SUCCEEDING!")
    nam=input("YOUR GOOD NAME PLZ:")
    gen=input("YOUR GENDER(F/M):")
    address=input("YOUR ADDRESS PLZ:")
    con=int(input("MAY WE KNOW YOUR CONTACT PLZ:"))
    date=input("TODAY'S DATE(DD-MM-YYYY):")
    print("HOW MAY WE HELP YOU?")
    tot=0
    st=""
    list1=[]
    list2=[]
    while True:
        options()
        op=int(input("ENTER YOUR RESPECTED ACTION NUMBER:"))
        if op in(1,2,3,4,5,6):
            if op==1:
                sandwich()
            elif op==2:
                snacks()          
            elif op==3:
                pastries()      
            elif op==4:
                chocolates()        
            elif op==5:
                others()
            elif op==6:
                chips()
            cod=input("ITEM CODE OF YOUR FAVOURITE ITEM:")
            n=int(input("NO. OF PLATES:"))
            df=pd.read_sql("select iprice*%s from bak where icode='%s'"%(n,cod),sqlco)
            s=pd.read_sql("select iname from bak where icode='%s'"%(cod),sqlco)
            print("YOU BOUGHT",n,"*",s.values) 
            print("YOUR AMOUNT IS:",df.values)
            tot=tot+df.values
            x=("update bak set availability=availability-%s where icode=%s")
            y=(n,cod)
            cu.execute(x,y)
            sqlco.commit()
            list1.append(str(s.values))
            list2.append(n)
            st=st+str(n)+str(s.values)+" "
            
        elif op==7:    
            combos()
            ch=int(input("NUMBER OF YOUR FAVOURITE COMBO:"))
            if ch==1:
                df1=pd.read_sql("select iprice*2 from bak where icode='d12'",sqlco)
                b=df1.values
                print("YOUR AMOUNT IS:",b)
                cu.execute("update bak set availability=availability-2 where icode='d12'")
                cu.execute("update bak set availability=availability-1 where icode='d42'")
                sqlco.commit()
            elif ch==2:
                df1=pd.read_sql("select iprice*3 from bak where icode='d22'",sqlco)
                b=df1.values
                print("YOUR AMOUNT IS:",b)
                cu.execute("update bak set availability=availability-3 where icode='d22'")
                cu.execute("update bak set availability=availability-1 where icode='d24'")
            elif ch==3:
                b=[80]
                print("YOUR AMOUNT IS:",b)
                cu.execute("update bak set availability=availability-2 where icode='d11'")
            list1.append("combo no.")
            list2.append(ch)
            tot=tot+b
            st=st+"combo no."+str(ch)+" "
            
            
        elif op in (8,9,10):
            if op==8:
                des()
            elif op==9:
                sr=pd.DataFrame({"ITEMS":list1,"PLATES":list2})
                print(sr)
            elif op==10:
                print("YOUR ORDER HAS BEEN RECEIVED SUCCESSFULLY!")
                break
    
    
          
        else:
            print("OOPS!SORRY,ACTION NOT AVAILABLE")


            
    print("YOUR FINALIZED ORDER IS:",st)
    print("YOUR TOTAL AMOUNT IS:",tot)


    
    deli()
    x=int(input("YOUR ACTION NUMBER:"))
    if x==1:
        mod="EAT IN"
        print("YOUR FOOD IS UNDER CONSTRUCTION! \nTHANKS FOR CHOOSING US!")
    elif x==2:
        mod="TAKEAWAY"
        print("YOUR FOOD IS UNDER CONSTRUCTION! \nTHANKS FOR CHOOSING US!")
    elif x==3:
        mod="HOME DELIVERY"
        print("YOU MAY TRACK YOUR ORDER WHEN IT WOULD BE DETACHED! \nTHANKS,HAVE A GOOD DAY!")

        
    
    amt=int(tot)
    add=("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s)")
    data=(nam,gen,address,con,date,st,amt,mod)
    cu.execute(add,data)
    sqlco.commit()    





entry()

sqlco.close()
cu.close()

if sqlco.is_connected():
    print(".......")
else:
    print("...")

from tkinter import*
from tkinter import messagebox
import os , math ,random 
class Super:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1300x700+30+10')
        self.root.title('Super_Market: سوبر ماركت')
        self.root.resizable(False,False)
        self.root.iconbitmap('Shopping bag gold logo vector image on VectorStock.ico')
        title = Label(self.root, text='ادارة المشاريع : سوبر ماركت',fg='white', bg='#0B2F3A',font=('tajawal',15))
        title.pack(fill=X)
        #====================Customer Data===========
        F1= Frame(root,bd=2,width=338,height=170,bg='#0B4C5F')
        F1.place(x=961,y=35)
        tit=Label(F1, text=' : بيانات المشتري  ' , font=('tajawal',13,'bold'), bg='#0B4c5F', fg='tomato')
        tit.place(x=185,y=0)
        his_name= Label(F1 , text=' اسم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_name.place(x=230,y=40)
        his_phone= Label(F1 , text=' رقم المشتري',font=('tajawal',10),bg='#0B4C5F',fg='white')
        his_phone.place(x=235,y=70)
        bill_num= Label(F1 , text=' رقم الفاتورة',font=('tajawal',10),bg='#0B4C5F',fg='white')
        bill_num.place(x=242,y=100)

        Ent_name = Entry(F1, justify='center')
        Ent_name.place(x=90,y=42)
        Ent_phone = Entry(F1, justify='center')
        Ent_phone.place(x=90,y=72)
        Ent_bill = Entry(F1, justify='center')
        Ent_bill.place(x=90,y=102)

        btn_customer = Button(F1 , text='Search' , font=('tajawal',10),width=10,height=4,bg='white')
        btn_customer.place(x=3,y=40)

        #============== Fatora bill ==============

        titdd = Label(F1 , text='[الفواتير]' , font=('tajawal',13,'bold') , bg='#0B4C5F' , fg='gold' )
        titdd.place(x=125,y=135)
        F3 = Frame(root,bd=2 , width=338 ,height=399 , bg='white')
        F3.place(x=961,y=205)
        scrol_y = Scrollbar(F3, orient=VERTICAL)
        self.textarea= Text(F3 ,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=LEFT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH , expand=1)
        #============ Price =============
        F4 = Frame(root, bd=2 , width=657, height=112 , bg='#0B4C5F')
        F4.place(x=641,y=587)
        hesab = Button(F4, text='الحساب', width=13, height=1 , font='tajawal', bg='#DBA901')
        hesab.place(x=520, y=10)
        fatora = Button(F4, text='تصدير الفاتورة' , width=13,height=1,font='tajawal',bg='#DBA901')
        fatora.place(x=520,y=55)
        clear = Button(F4, text='افراغ الحقول' , width= 13,height=1 , font='tajawal', bg='#DBA901')
        clear.place(x=375,y=10)
        exit = Button(F4, text='اغلاق البرنامج', width=13,height=1,font='tajawal',bg='#DBA901' )
        exit.place(x=375, y=55)
        
        
        lb101 = Label(F4, text='حساب الكلي للبقوليات', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb101.place(x=220,y=10)

        lb102 = Label(F4, text='حساب اللوازم المنزليه', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb102.place(x=220,y=40)

        lb103 = Label(F4, text='حساب ادوات الكهرباء', font=('tajawal',10,'bold'), bg='#0B4C5F',fg='gold')
        lb103.place(x=220,y=70)


        ento1 = Entry(F4, width=24)
        ento1.place(x=40, y=12)

        ento2 = Entry(F4, width=24)
        ento2.place(x=40, y=42)

        ento3 = Entry(F4,width=24)
        ento3.place(x=40, y=72)

        #============= items[1] ============
        FF1=Frame(root, bd=2 , width=318, height=664,bg='#0B4C5F')
        FF1.place(x=1,y=35)
        t = Label(FF1, text='البقوليات', font=('tajawal',13,'bold'), bg='#0B4C5F' , fg='gold')
        t.place(x=122,y=0)
        bq1 = Label(FF1, text='الرز', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq1.place(x=250,y=50)

        bq2 = Label(FF1, text='برغل', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq2.place(x=240,y=80)

        bq3 = Label(FF1, text='فاصولياء', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq3.place(x=210,y=110)

        bq4 = Label(FF1, text='عدس', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq4.place(x=232,y=140)

        bq5 = Label(FF1, text='مكرونة', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq5.place(x=213,y=170)

        bq6 = Label(FF1, text='حمص', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq6.place(x=233,y=200)

        bq7 = Label(FF1, text='فول', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq7.place(x=228,y=230)

        bq8 = Label(FF1, text='الملح', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq8.place(x=240,y=270)

        bq9 = Label(FF1, text='سكر', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq9.place(x=230,y=300)

        bq10 = Label(FF1, text='فلفل اسود', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq10.place(x=233,y=330)

        bq11 = Label(FF1, text='اللوبيا', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq11.place(x=200,y=370)

        bq12 = Label(FF1, text='فلفل احمر', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq12.place(x=200,y=400)

        bq13 = Label(FF1, text='كمون', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq13.place(x=230,y=430)

        bq14 = Label(FF1, text='قمح', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq14.place(x=210,y=470)

        bq15 = Label(FF1, text='شعير', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq15.place(x=230,y=500)

        bq16 = Label(FF1, text='شوفان', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq16.place(x=220,y=530)

        bq17 = Label(FF1, text='ذرة', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq17.place(x=230,y=570)

        bq18 = Label(FF1, text='اللوبيا', font=('tajawal',11), bg='#0B4C5F',fg='white' )
        bq18.place(x=230,y=600)

        bqent1= Entry (FF1, width=12)
        bqent1.place(x=70,y=50)

        bqent2= Entry (FF1, width=12)
        bqent2.place(x=70,y=80)

        bqent3= Entry (FF1, width=12)
        bqent3.place(x=70,y=110)

        bqent4= Entry (FF1, width=12)
        bqent4.place(x=70,y=140)

        bqent5= Entry (FF1, width=12)
        bqent5.place(x=70,y=170)

        bqent6= Entry (FF1, width=12)
        bqent6.place(x=70,y=200)

        bqent7= Entry (FF1, width=12)
        bqent7.place(x=70,y=230)

        bqent8= Entry (FF1, width=12)
        bqent8.place(x=70,y=270)

        bqent9= Entry (FF1, width=12)
        bqent9.place(x=70,y=300)

        bqent10= Entry (FF1, width=12)
        bqent10.place(x=70,y=330)

        bqent11= Entry (FF1, width=12)
        bqent11.place(x=70,y=370)

        bqent12= Entry (FF1, width=12)
        bqent12.place(x=70,y=400)

        bqent13= Entry (FF1, width=12)
        bqent13.place(x=70,y=430)

        bqent14= Entry (FF1, width=12)
        bqent14.place(x=70,y=470)

        bqent15= Entry (FF1, width=12)
        bqent15.place(x=70,y=500)

        bqent16= Entry (FF1, width=12)
        bqent16.place(x=70,y=530)

        bqent17= Entry (FF1, width=12)
        bqent17.place(x=70,y=570)

        bqent18= Entry (FF1, width=12)
        bqent18.place(x=70,y=600)


        #---------items (2)-------#
        FF2=Frame(root, bd=2 , width=318, height=664,bg='#0B4C5F')
        FF2.place(x=321,y=35)
        tt= Label(FF2, text='اللوازم المنزليه', font=('tajawal',13,'bold'), bg='#0B4C5F' , fg='gold')
        tt.place(x=120,y=0)
        bqr1 = Label(FF2, text='مصفاه', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr1.place(x=228,y=50)

        bqr2 = Label(FF2, text='طبق', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr2.place(x=233,y=80)

        bqr3 = Label(FF2, text='مج', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr3.place(x=234,y=110)

        bqr4 = Label(FF2, text='براد شاي', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr4.place(x=237,y=140)

        bqr5 = Label(FF2, text='سكينه', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr5.place(x=227,y=170)

        bqr6 = Label(FF2, text='شوكه', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr6.place(x=233,y=200)

        bqr7 = Label(FF2, text='حله', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr7.place(x=228,y=230)

        bqr8 = Label(FF2, text='سله', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr8.place(x=240,y=270)

        bqr9 = Label(FF2, text='معالق', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr9.place(x=230,y=300)

        bqr10 = Label(FF2, text=' صينيه', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr10.place(x=233,y=330)

        bqr11 = Label(FF2, text='خلاط', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr11.place(x=200,y=370)

        bqr12 = Label(FF2, text=' فتاحه علب', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr12.place(x=200,y=400)

        bqr13 = Label(FF2, text='مقشرة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr13.place(x=220,y=430)

        bqr14 = Label(FF2, text='لوح تقطيع', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr14.place(x=190,y=470)

        bqr15 = Label(FF2, text='مقوار', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr15.place(x=230,y=500)

        bqr16 = Label(FF2, text='سلة قمامة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr16.place(x=190,y=530)

        bqr17 = Label(FF2, text='منفضة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr17.place(x=219,y=570)

        bqr18 = Label(FF2, text='أكياس', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        bqr18.place(x=225,y=600)

        bqrnt1= Entry (FF2, width=12)
        bqrnt1.place(x=70,y=50)

        bqrnt2= Entry (FF2, width=12)
        bqrnt2.place(x=70,y=80)

        bqrnt3= Entry (FF2, width=12)
        bqrnt3.place(x=70,y=110)

        bqrnt4= Entry (FF2, width=12)
        bqrnt4.place(x=70,y=140)

        bqrnt5= Entry (FF2, width=12)
        bqrnt5.place(x=70,y=170)

        bqrnt6= Entry (FF2, width=12)
        bqrnt6.place(x=70,y=200)

        bqrnt7= Entry (FF2, width=12)
        bqrnt7.place(x=70,y=230)

        bqrnt8= Entry (FF2, width=12)
        bqrnt8.place(x=70,y=270)

        bqrnt9= Entry (FF2, width=12)
        bqrnt9.place(x=70,y=300)

        bqrnt10= Entry (FF2, width=12)
        bqrnt10.place(x=70,y=330)

        bqrnt11= Entry (FF2, width=12)
        bqrnt11.place(x=70,y=370)

        bqrnt12= Entry (FF2, width=12)
        bqrnt12.place(x=70,y=400)

        bqrnt13= Entry (FF2, width=12)
        bqrnt13.place(x=70,y=430)

        bqrnt14= Entry (FF2, width=12)
        bqrnt14.place(x=70,y=470)

        bqrnt15= Entry (FF2, width=12)
        bqrnt15.place(x=70,y=500)

        bqrnt16= Entry (FF2, width=12)
        bqrnt16.place(x=70,y=530)

        bqrnt17= Entry (FF2, width=12)
        bqrnt17.place(x=70,y=570)

        bqrnt18= Entry (FF2, width=12)
        bqrnt18.place(x=70,y=600)

        #--------- items (3)--------#


        FF3=Frame(root, bd=2 , width=318, height=550,bg='#0B4C5F')
        FF3.place(x=641,y=35)
        ttt= Label(FF3, text=' أدوات كهربية', font=('tajawal',13,'bold'), bg='#0B4C5F' , fg='gold')
        ttt.place(x=120,y=0)
        br1 = Label(FF3, text='مكنسة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br1.place(x=228,y=50)

        br2 = Label(FF3, text='تليفزيون', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br2.place(x=233,y=80)

        br3 = Label(FF3, text='غسالة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br3.place(x=234,y=110)

        br4 = Label(FF3, text=' ميكرويف', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br4.place(x=230,y=140)

        br5 = Label(FF3, text='خلاط', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br5.place(x=243,y=170)

        br6 = Label(FF3, text='فرن غاز', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br6.place(x=233,y=200)

        br7 = Label(FF3, text='مقلاة كهرباء', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br7.place(x=195,y=230)

        br8 = Label(FF3, text='مروحة سقف', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br8.place(x=200,y=270)

        br9 = Label(FF3, text='مروحة أرضية', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br9.place(x=200,y=300)

        br10 = Label(FF3, text='  سخان', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br10.place(x=210,y=330)

        br11 = Label(FF3, text=' شاشة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br11.place(x=210,y=370)

        br12 = Label(FF3, text='  فلتر ماء', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br12.place(x=230,y=400)

        br13 = Label(FF3, text='تلاجة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br13.place(x=210,y=430)

        br14 = Label(FF3, text=' مكواة', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br14.place(x=240,y=470)

        br15 = Label(FF3, text='تكييف', font=('tajawal',12), bg='#0B4C5F',fg='white' )
        br15.place(x=243,y=500)

        bqnt1= Entry (FF3, width=12)
        bqnt1.place(x=70,y=50)

        bqnt2= Entry (FF3, width=12)
        bqnt2.place(x=70,y=80)

        bqnt3= Entry (FF3, width=12)
        bqnt3.place(x=70,y=110)

        bqnt4= Entry (FF3, width=12)
        bqnt4.place(x=70,y=140)

        bqnt5= Entry (FF3, width=12)
        bqnt5.place(x=70,y=170)

        bqnt6= Entry (FF3, width=12)
        bqnt6.place(x=70,y=200)

        bqnt7= Entry (FF3, width=12)
        bqnt7.place(x=70,y=230)

        bqnt8= Entry (FF3, width=12)
        bqnt8.place(x=70,y=270)

        bqnt9= Entry (FF3, width=12)
        bqnt9.place(x=70,y=300)

        bqnt10= Entry (FF3, width=12)
        bqnt10.place(x=70,y=330)

        bqnt11= Entry (FF3, width=12)
        bqnt11.place(x=70,y=370)

        bqnt12= Entry (FF3, width=12)
        bqnt12.place(x=70,y=400)

        bqnt13= Entry (FF3, width=12)
        bqnt13.place(x=70,y=430)

        bqnt14= Entry (FF3, width=12)
        bqnt14.place(x=70,y=470)

        bqnt15= Entry (FF3, width=12)
        bqnt15.place(x=70,y=500)

        
























root=Tk()
ob = Super(root)
root.mainloop()
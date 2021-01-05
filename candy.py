import random
global puan
global anahtar
global puan_anahtar
global matris
global yapaymatris
global ipucu_i
global ipucu_j
global ipucu_yon
global matris_uzunluk
global olusturma_puan_kilit
global bolum_anahtar
global bolum_anahtar2
global bolum_anahtar3
global bolum_anahtar4

bolum_anahtar=True
bolum_anahtar2=True
bolum_anahtar3=True
bolum_anahtar4=True




matris_uzunluk=5

puan_anahtar=False
anahtar=False

puan=0
matris=[[0 for j in range(5)] for i in range(5)]
yapaymatris=[[0 for j in range(5)] for i in range(5)]

def olusturma():
    global bolum_anahtar
    global bolum_anahtar2
    global bolum_anahtar3
    global bolum_anahtar4

    global olusturma_puan_kilit
    global puan
    global matris_uzunluk
    global matris
    global yapaymatris
    #print 'olusturma'
    #p=1
    #for i in range(5):
    #    for j in range(5):
    #        matris[i][j]=p
    #        if p>=4:
    #            p=0
    #        p=p+1
    if puan==0 and bolum_anahtar==True:
        bolum_anahtar=False
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                renk=random.randint(1,4)
                matris[i][j]=renk
        #yazdirma()
        olusturma_puan_kilit=False
        kontrol()
        olusturma_puan_kilit=True


                

    elif puan>200 and bolum_anahtar2==True:
        bolum_anahtar2=False
        matris_uzunluk=10
        matris=[[0 for j in range(matris_uzunluk)] for i in range(matris_uzunluk)]
        yapaymatris=[[0 for j in range(matris_uzunluk)] for i in range(matris_uzunluk)]
        
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                renk=random.randint(1,6)
                matris[i][j]=renk

        olusturma_puan_kilit=False

        kontrol()
        olusturma_puan_kilit=True

    
    elif puan>300 and bolum_anahtar3==True:
        bolum_anahtar3=False
        matris_uzunluk=15
        matris=[[0 for j in range(matris_uzunluk)] for i in range(matris_uzunluk)]
        yapaymatris=[[0 for j in range(matris_uzunluk)] for i in range(matris_uzunluk)]
        
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                renk=random.randint(1,8)
                matris[i][j]=renk

        olusturma_puan_kilit=False

        kontrol()
        olusturma_puan_kilit=True




    
    


def kontrol():
    #print 'kontrol'
    ikontrol()
    jkontrol()

def ikontrol():
    global matris_uzunluk
    #print 'ikontrol'
    global anahtar
    global puan_anahtar
    global puan
    for j in range(matris_uzunluk):
        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=5)and (matris[i][j]==matris[i+1][j]==matris[i+2][j]==matris[i+3][j]==matris[i+4][j]):
                #yazdirma()
                matris[i][j]=0
                matris[i+1][j]=0
                matris[i+2][j]=0
                matris[i+3][j]=0
                matris[i+4][j]=0
                anahtar=True
                yazdirma()
                ikaydirma(i+4,j,5)#3 deger gönderilir sonuncu deger ise kac adet yok edildigi
                #yazdirma()

                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=50
                    yazdirma()
                
                
        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=4)and  (matris[i][j]==matris[i+1][j]==matris[i+2][j]==matris[i+3][j]):
                #yazdirma()
                matris[i][j]=0
                matris[i+1][j]=0
                matris[i+2][j]=0
                matris[i+3][j]=0
                anahtar=True
                yazdirma()
                ikaydirma(i+3,j,4)
                #yazdirma()
                
                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=40
                    yazdirma()
                

        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=3)and (matris[i][j]==matris[i+1][j]==matris[i+2][j]):
                #yazdirma()
                matris[i][j]=0
                matris[i+1][j]=0
                matris[i+2][j]=0
                anahtar=True
                yazdirma()
                ikaydirma(i+2,j,3)
                #yazdirma()
                
                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=30
                    yazdirma()
                




        

def jkontrol():
    global matris_uzunluk
    #print 'jkontrol'
    global anahtar
    global puan_anahtar
    global puan
    for i in range(matris_uzunluk):
        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=5)and (matris[i][j]==matris[i][j+1]==matris[i][j+2]==matris[i][j+3]==matris[i][j+4]):
                #yazdirma()
                matris[i][j]=0
                matris[i][j+1]=0
                matris[i][j+2]=0
                matris[i][j+3]=0
                matris[i][j+4]=0
                yazdirma()
                jkaydirma(i,j+4,5)
                anahtar=True
                #yazdirma()
                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=50
                    yazdirma()
                
                
                
        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=4)and  (matris[i][j]==matris[i][j+1]==matris[i][j+2]==matris[i][j+3]):
                #yazdirma()
                matris[i][j]=0
                matris[i][j+1]=0
                matris[i][j+2]=0
                matris[i][j+3]=0
                anahtar=True
                yazdirma()
                jkaydirma(i,j+3,4)
                #yazdirma()
                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=40
                    yazdirma()
                

        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=3)and(matris[i][j]==matris[i][j+1]==matris[i][j+2]):
                #yazdirma()
                matris[i][j]=0
                matris[i][j+1]=0
                matris[i][j+2]=0
                anahtar=True
                yazdirma()
                jkaydirma(i,j+2,3)
                #yazdirma()
                
                
                if puan_anahtar==True and olusturma_puan_kilit==True:
                    puan+=30
                    yazdirma()
                
    
def ikaydirma(i,j,k):
    #print 'ikaydirma'
    sayi=k
    for y in range(sayi):
        for x in range(i,0,-1):
            aktarma=matris[x][j]
            matris[x][j]=matris[x-1][j]
            matris[x-1][j]=aktarma
    rastgele()
    


def jkaydirma(i,j,k):
    #print 'jkaydirma'
    for z in range(j,j-k,-1):
        for x in range(i,0,-1):
            aktarma=matris[x][z]
            matris[x][z]=matris[x-1][z]
            matris[x-1][z]=aktarma
    rastgele()

def rastgele():
    global puan
    global matris_uzunluk
    #print 'rastgele'
    if puan<=200:
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if matris[i][j]==0:
                    rastgele=random.randint(1,4)
                    matris[i][j]=rastgele
                else:
                    pass
    elif puan<=300:
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if matris[i][j]==0:
                    rastgele=random.randint(1,6)
                    matris[i][j]=rastgele
                else:
                    pass
    elif puan<=400:
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if matris[i][j]==0:
                    rastgele=random.randint(1,8)
                    matris[i][j]=rastgele
                else:
                    pass
    elif puan>400:
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if matris[i][j]==0:
                    rastgele=random.randint(1,10)
                    matris[i][j]=rastgele
                else:
                    pass
    kontrol()

def yerdegis(i,j,yon):
    #print 'yerdegis'
    global puan_anahtar
    global anahtar
    puan_anahtar=True
    deger=False
    anahtar=False
    if i>0 and yon=='w':
        aktarma=matris[i][j]
        matris[i][j]=matris[i-1][j]
        matris[i-1][j]=aktarma
        deger=True
    elif i<(matris_uzunluk-1) and yon=='s':
        aktarma=matris[i][j]
        matris[i][j]=matris[i+1][j]
        matris[i+1][j]=aktarma
        deger=True
    elif j>0 and yon=='a':
        aktarma=matris[i][j]
        matris[i][j]=matris[i][j-1]
        matris[i][j-1]=aktarma
        deger=True
    elif j<(matris_uzunluk-1)and yon=='d':
        aktarma=matris[i][j]
        matris[i][j]=matris[i][j+1]
        matris[i][j+1]=aktarma
        deger=True
        
    kontrol()

    
    if anahtar==False and deger==True:
        if yon=='w':
            aktarma=matris[i-1][j]
            matris[i-1][j]=matris[i][j]
            matris[i][j]=aktarma
            deger=True
        elif yon=='s':
            aktarma=matris[i+1][j]
            matris[i+1][j]=matris[i][j]
            matris[i][j]=aktarma
            deger=True
        elif yon=='a':
            aktarma=matris[i][j-1]
            matris[i][j-1]=matris[i][j]
            matris[i][j]=aktarma
            deger=True
        elif yon=='d':
            aktarma=matris[i][j+1]
            matris[i][j+1]=matris[i][j]
            matris[i][j]=aktarma
            deger=True
        else:
            pass
        
        print "\n***Puan alacak bir sey yok baska oyna***"
        
    elif anahtar==True:
        print "guzel puan aldin"
        





######################################################################################################
def esitleme():
    global matris_uzunluk
    global matris
    global yapaymatris
    
    for i in range(matris_uzunluk):
        for j in range(matris_uzunluk):
            yapaymatris[i][j]=matris[i][j]


        
def oyundevam_kontrol():
    global matris_uzunluk
    #yazdirma()
    #print 'oyundevam_kontrol'
    global matris
    global yapaymatris
    esitleme()
            
    for x in range(1,5):
        
        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if i>0 and x==1:
                    aktarma=yapaymatris[i][j]
                    yapaymatris[i][j]=yapaymatris[i-1][j]
                    yapaymatris[i-1][j]=aktarma
                    yapay=yapaykontrol()
                    if yapay==True:
                        ipucu_kayit(i,j,x)
                        return True
                    else:
                        esitleme()


        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if i<(matris_uzunluk-1) and x==2:
                    aktarma=yapaymatris[i][j]
                    yapaymatris[i][j]=yapaymatris[i+1][j]
                    yapaymatris[i+1][j]=aktarma
                    yapay=yapaykontrol()
                    if yapay==True:
                        ipucu_kayit(i,j,x)
                        return True
                    else:
                        esitleme()


        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if j>0 and x==3:
                    aktarma=yapaymatris[i][j]
                    yapaymatris[i][j]=yapaymatris[i][j-1]
                    yapaymatris[i][j-1]=aktarma
                    yapay=yapaykontrol()
                    if yapay==True:
                        ipucu_kayit(i,j,x)
                        return True
                    else:
                        esitleme()


        for i in range(matris_uzunluk):
            for j in range(matris_uzunluk):
                if j<(matris_uzunluk-1) and x==4:
                    aktarma=yapaymatris[i][j]
                    yapaymatris[i][j]=yapaymatris[i][j+1]
                    yapaymatris[i][j+1]=aktarma
                    yapay=yapaykontrol()
                    if yapay==True:
                        ipucu_kayit(i,j,x)
                        return True
                    else:
                        esitleme()

    return False
    #yazdirma()

    

def yapaykontrol():
    #yazdirma()
    #print 'yapaykontrol'
    i=iyapaykontrol()
    j=jyapaykontrol()
    if i==True or j==True:
        #print "yapay kontrol***********if***********************"
        #yazdirma()
        #print "yapay kontrol************if**********************"
    
        return True
    
    else:
        #print "yapay kontrol************else**********************"
        #yazdirma()
        #print "yapay kontrol*************else*********************"
        return False
    


def iyapaykontrol():
    global matris_uzunluk
    #yazdirma()
    global yapaymatris
    #print 'iyapayakontrol'
    for j in range(matris_uzunluk):
        
        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=5)and (yapaymatris[i][j]==yapaymatris[i+1][j]==yapaymatris[i+2][j]==yapaymatris[i+3][j]==yapaymatris[i+4][j]):
                #print "iyapay besli","i=",i,"j=",j
                return True

                
        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=4)and  (yapaymatris[i][j]==yapaymatris[i+1][j]==yapaymatris[i+2][j]==yapaymatris[i+3][j]):
                #print "iyapay dortlu","i=",i,"j=",j
                return True


        for i in range(matris_uzunluk):
            if (matris_uzunluk-i>=3)and  (yapaymatris[i][j]==yapaymatris[i+1][j]==yapaymatris[i+2][j]):
                #print "iyapay uclu","i=",i,"j=",j
                return True

                
    return False

    

def jyapaykontrol():
    global matris_uzunluk
    #yazdirma()
    global yapaymatris
    #print 'jyapaykontrol'
    global yapaymatris
    for i in range(matris_uzunluk):
        
        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=5)and (yapaymatris[i][j]==yapaymatris[i][j+1]==yapaymatris[i][j+2]==yapaymatris[i][j+3]==yapaymatris[i][j+4]):
                return True


                
        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=4)and (yapaymatris[i][j]==yapaymatris[i][j+1]==yapaymatris[i][j+2]==yapaymatris[i][j+3]):
                return True


        for j in range(matris_uzunluk):
            if (matris_uzunluk-j>=3)and (yapaymatris[i][j]==yapaymatris[i][j+1]==yapaymatris[i][j+2]):
                return True

            
    return False


def ipucu_kayit(i,j,x):
    global ipucu_i
    global ipucu_j
    global ipucu_yon
    ipucu_i=i
    ipucu_j=j
    ipucu_yon=x
    
    if x==1:
        ipucu_yon="yukari"
        
    elif x==2:
        ipucu_yon="asagi"
        
    elif x==3:
        ipucu_yon="sola"
        
    elif x==4:
        ipucu_yon="saga"

    
    
####################################################################################################################################



    
def yazdirma():
    global matris_uzunluk
    #print 'yazdirma'
    global puan
    print "puan=",puan
    print "    ^"
    print "    w"
    print "< a","s","d >"
    print "    v"
    for i in range(matris_uzunluk):
        print '\t',i,
    print ''
    for i in range(matris_uzunluk):
        print '\t_',
    print ''
    print ''
    for i in range(matris_uzunluk):          
        for j in range(matris_uzunluk):
            if j==0:
                print i,'|','\t',
            if matris[i][j]==1:
                print 'M','\t',
            elif matris[i][j]==2:
                print 'S','\t',
            elif matris[i][j]==3:
                print 'Y','\t',
            elif matris[i][j]==4:
                print 'K','\t',
            elif matris[i][j]==5:
                print 'B','\t',
            elif matris[i][j]==6:
                print 'T','\t',
            elif matris[i][j]==7:
                print 'G','\t',
            elif matris[i][j]==8:
                print 'E','\t',
            elif matris[i][j]==9:
                print 'P','\t',
            elif matris[i][j]==10:
                print 'A','\t',
            elif matris[i][j]==0:
                print '0','\t',
            
        print '\n'

def tekrar():
    #print 'tekrar'
    global puan
    print "puan=",puan
    basla=raw_input("baslamak icin 'r' basin:")
    if basla=='r':
        anayer()
    else:
        pass

def anayer():
    global ipucu_i
    global ipucu_j
    global ipucu_yon
    #print 'anayer'
    global puan
    puan=0
    olusturma()
    oyun=oyundevam_kontrol()
    while oyun==True:
        oyundevam_kontrol()
        kontrol()
        yazdirma()
        print "***************ipucu icin '88' basin"
        ssatir=input("lutfen satir girin:")        
        if ssatir==88:
            print ipucu_i,".satir",ipucu_j,".sutun",ipucu_yon
            ssatir=input("lutfen satir girin:")
            sutun=input("lutfen sutun girin:")
            yon=raw_input("lutfen yon girin:(w,a,s,d:)")
        else:
            sutun=input("lutfen sutun girin:")
            yon=raw_input("lutfen yon girin:(w,a,s,d):")
        yerdegis(ssatir,sutun,yon)
        kontrol()
        oyun=oyundevam_kontrol()
        olusturma()
    tekrar()
    
        
anayer()

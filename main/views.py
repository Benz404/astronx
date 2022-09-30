from django.shortcuts import render,get_object_or_404
from main.models import audit_wealth
from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    return render(request,'index.html')

#####################################################################################

def about(request):
    return render(request,'about.html')

######################################################################################

def audit(request,*args, **kwargs):
    if request.method=="POST":
        stnm1=request.POST['stnm1']
        stnm2=request.POST['stnm2']
        stnm3=request.POST['stnm3']
        stnm4=request.POST['stnm4']
        stnm5=request.POST['stnm5']
        stnm6=request.POST['stnm6']
        stnm7=request.POST['stnm7']
        stnm8=request.POST['stnm8']
        stnm9=request.POST['stnm9']
        stnm10=request.POST['stnm10']
        stbp1=request.POST['stbp1']
        stbp2=request.POST['stbp2']
        stbp3=request.POST['stbp3']
        stbp4=request.POST['stbp4']
        stbp5=request.POST['stbp5']
        stbp6=request.POST['stbp6']
        stbp7=request.POST['stbp7']
        stbp8=request.POST['stbp8']
        stbp9=request.POST['stbp9']
        stbp10=request.POST['stbp10']
        stam1=request.POST['stam1']
        stam2=request.POST['stam2']
        stam3=request.POST['stam3']
        stam4=request.POST['stam4']
        stam5=request.POST['stam5']
        stam6=request.POST['stam6']
        stam7=request.POST['stam7']
        stam8=request.POST['stam8']
        stam9=request.POST['stam9']
        stam10=request.POST['stam10']
        stcp1=request.POST['stcp1']
        stcp2=request.POST['stcp2']
        stcp3=request.POST['stcp3']
        stcp4=request.POST['stcp4']
        stcp5=request.POST['stcp5']
        stcp6=request.POST['stcp6']
        stcp7=request.POST['stcp7']
        stcp8=request.POST['stcp8']
        stcp9=request.POST['stcp9']
        stcp10=request.POST['stcp10']
        mfnm1=request.POST['mfnm1']
        mfnm2=request.POST['mfnm2']
        mfnm3=request.POST['mfnm3']
        mfnm4=request.POST['mfnm4']
        mfnm5=request.POST['mfnm5']
        mfia1=request.POST['mfia1']
        mfia2=request.POST['mfia2']
        mfia3=request.POST['mfia3']
        mfia4=request.POST['mfia4']
        mfia5=request.POST['mfia5']
        mfca1=request.POST['mfca1']
        mfca2=request.POST['mfca2']
        mfca3=request.POST['mfca3']
        mfca4=request.POST['mfca4']
        mfca5=request.POST['mfca5']
        cynm1=request.POST['cynm1']
        cynm2=request.POST['cynm2']
        cynm3=request.POST['cynm3']
        cynm4=request.POST['cynm4']
        cynm5=request.POST['cynm5']
        cyia1=request.POST['cyia1']
        cyca1=request.POST['cyca1']
        cyia2=request.POST['cyia2']
        cyca2=request.POST['cyca2']
        cyia3=request.POST['cyia3']
        cyca3=request.POST['cyca3']
        cyia4=request.POST['cyia4']
        cyca4=request.POST['cyca4']
        cyia5=request.POST['cyia5']
        cyca5=request.POST['cyca5']
        bnnm1=request.POST['bnnm1']
        bnbl1=request.POST['bnbl1']
        bnnm2=request.POST['bnnm2']
        bnbl2=request.POST['bnbl2']
        bnnm3=request.POST['bnnm3']
        bnbl3=request.POST['bnbl3']
        csbl=request.POST['csbl']
        dmbl=request.POST['dmbl']
        brnm1=request.POST['brnm1']
        bram1=request.POST['bram1']
        lnnm1=request.POST['lnnm1']
        lnam1=request.POST['lnam1']
        brnm2=request.POST['brnm2']
        bram2=request.POST['bram2']
        lnnm2=request.POST['lnnm2']
        lnam2=request.POST['lnam2']
        brnm3=request.POST['brnm3']
        bram3=request.POST['bram3']
        lnnm3=request.POST['lnnm3']
        lnam3=request.POST['lnam3']
        ###################################################################################################################################
        total_stocks_investment=((float(stbp1)*float(stam1))+(float(stbp2)*float(stam2))+(float(stbp3)*float(stam3))+(float(stbp4)*float(stam4))+(float(stbp5)*float(stam5))+(float(stbp6)*float(stam6))+(float(stbp7)*float(stam7))+(float(stbp8)*float(stam8))+(float(stbp9)*float(stam9))+(float(stbp10)*float(stam10)))
        total_stocks_return=((float(stcp1)*float(stam1))+(float(stcp2)*float(stam2))+(float(stcp3)*float(stam3))+(float(stcp4)*float(stam4))+(float(stcp5)*float(stam5))+(float(stcp6)*float(stam6))+(float(stcp7)*float(stam7))+(float(stcp8)*float(stam8))+(float(stcp9)*float(stam9))+(float(stcp10)*float(stam10)))
        mutual_fund_investment=(float(mfia1)+float(mfia2)+float(mfia3)+float(mfia4)+float(mfia5))
        mutual_fund_return=(float(mfca1)+float(mfca2)+float(mfca3)+float(mfca4)+float(mfca5))
        crypto_investment=(float(cyia1)+float(cyia2)+float(cyia3)+float(cyia4)+float(cyia5))
        crypto_return=(float(cyca1)+float(cyca2)+float(cyca3)+float(cyca4)+float(cyca5))
        bank_balance=float(bnbl1)+float(bnbl2)+float(bnbl3)
        Hand_cash=float(csbl)
        demat_balance=float(dmbl)
        total_borrow_money=float(bram1)+float(bram2)+float(bram3)
        total_lend_money=float(lnam1)+float(lnam2)+float(lnam3)
        total_investment=total_stocks_investment+mutual_fund_investment+crypto_investment+bank_balance+Hand_cash+demat_balance-total_borrow_money+total_lend_money
        total_return=total_stocks_return+mutual_fund_return+crypto_return+bank_balance+Hand_cash+demat_balance-total_borrow_money+total_lend_money
        total_profit=total_return-total_investment
        ###################################################################################################################################
        total_stock_profit=total_stocks_return-total_stocks_investment
        total_mutual_fund_profit=mutual_fund_return-mutual_fund_investment
        total_crypto_profit=crypto_return-crypto_investment
        ##################################################################################################################################
        data=audit_wealth(st_name_1=stnm1,st_buy_price_1=stbp1,st_amount_1=stam1,st_current_price_1=stcp1,st_name_2=stnm2,st_buy_price_2=stbp2,st_amount_2=stam2,st_current_price_2=stcp2,st_name_3=stnm3,st_buy_price_3=stbp3,st_amount_3=stam3,st_current_price_3=stcp3,st_name_4=stnm4,st_buy_price_4=stbp4,st_amount_4=stam4,st_current_price_4=stcp4,st_name_5=stnm5,st_buy_price_5=stbp5,st_amount_5=stam5,st_current_price_5=stcp5,st_name_6=stnm6,st_buy_price_6=stbp6,st_amount_6=stam6,st_current_price_6=stcp6,st_name_7=stnm7,st_buy_price_7=stbp7,st_amount_7=stam7,st_current_price_7=stcp7,st_name_8=stnm8,st_buy_price_8=stbp8,st_amount_8=stam8,st_current_price_8=stcp8,st_name_9=stnm9,st_buy_price_9=stbp9,st_amount_9=stam9,st_current_price_9=stcp9,st_name_10=stnm10,st_buy_price_10=stbp10,st_amount_10=stam10,st_current_price_10=stcp10,mf_name_1=mfnm1,mf_invested_1=mfia1,mf_current_1=mfca1,mf_name_2=mfnm2,mf_invested_2=mfia2,mf_current_2=mfca2,mf_name_3=mfnm3,mf_invested_3=mfia3,mf_current_3=mfca3,mf_name_4=mfnm4,mf_invested_4=mfia4,mf_current_4=mfca4,mf_name_5=mfnm5,mf_invested_5=mfia5,mf_current_5=mfca5,cy_name_1=cynm1,cy_invested_1=cyia1,cy_current_1=cyca1,cy_name_2=cynm2,cy_invested_2=cyia2,cy_current_2=cyca2,cy_name_3=cynm3,cy_invested_3=cyia3,cy_current_3=cyca3,cy_name_4=cynm4,cy_invested_4=cyia4,cy_current_4=cyca4,cy_name_5=cynm5,cy_invested_5=cyia5,cy_current_5=cyca5,bank_name_1=bnnm1,bank_balance_1=bnbl1,bank_name_2=bnnm2,bank_balance_2=bnbl2,bank_name_3=bnnm3,bank_balance_3=bnbl3,hand_balance=csbl,demat_balance=dmbl,person_name_borrow_1=brnm1,borrow_money_1=bram1,person_name_borrow_2=brnm2,borrow_money_2=bram2,person_name_borrow_3=brnm3,borrow_money_3=bram3,person_name_lend_1=lnnm1,lend_money_1=lnam1,person_name_lend_2=lnnm2,lend_money_2=lnam2,person_name_lend_3=lnnm3,lend_money_3=lnam3,total_stock_investment=total_stocks_investment,total_stock_return=total_stocks_return,total_Mutual_fund_investment=mutual_fund_investment,total_Mutual_fund_return=mutual_fund_return,total_crypto_investment=crypto_investment,total_crypto_return=crypto_return,total_borrow=total_borrow_money,total_lend=total_lend_money,total_bank_balance=bank_balance,total_investment=total_investment,total_return=total_return,total_profit=total_profit,total_stock_profit=total_stock_profit,total_Mutual_fund_profit=total_mutual_fund_profit,total_crypto_profit=total_crypto_profit)
        data.save()
        print(data)
        ###################################################################################################################################
        carrier_data={
            'ttstin':total_stocks_investment,
            'ttstrt':total_stocks_return,
            'ttmfin':mutual_fund_investment,
            'ttmfrt':mutual_fund_return,
            'ttcyin':crypto_investment,
            'ttcyrt':crypto_return,
            'tthc':Hand_cash,
            'ttdm':demat_balance,
            'ttbn':bank_balance,
            'ttbm':total_borrow_money,
            'ttlm':total_lend_money,
            'ttin':total_investment,
            'ttrt':total_return
        }
        return render(request,'submit.html',carrier_data)
    return render(request,'audit.html')

######################################################################################
def database(request,*args, **kwargs):
    stored_data=audit_wealth.objects.all().order_by('-created')
    dna_data={
        'dataline':stored_data,
    }
    return render(request,'database.html',dna_data)

######################################################################################

def detail(request,pk):
  data = get_object_or_404(audit_wealth, pk=pk)
  context = {
      "data":data
  }
  return render(request, "details.html", context)

######################################################################################

def graph(request,*args, **kwargs):
    info=audit_wealth.objects.all()
    dna_data={
        'dataline':info
    }
    return render(request,'graph.html',dna_data)

######################################################################################
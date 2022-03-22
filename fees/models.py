from django.db import models

# Create your models here.
class Summary01(models.Model):
    BRANCH = models.CharField(max_length=200)
    ATMNAME = models.CharField(max_length=100, blank=True, null=True)
    PRODUCTNAME = models.CharField(max_length=200, blank=True, null=True)
    TERMINALID = models.CharField(max_length=10, null=True, blank=True)
    LOGNO = models.IntegerField(blank=True, null=True)
    ATMCOUNT = models.IntegerField(null=True, default= 0)
    ATMAMOUNT = models.IntegerField(null=True, default= 0)
    ATMFEE = models.IntegerField(null=True, default= 0)
    BALCOUNT = models.IntegerField(null=True, blank=True)
    BALFEE = models.IntegerField(null=True, blank=True)
    MINICOUNT = models.IntegerField(null=True, blank=True)
    MINIFEE = models.IntegerField( null=True, blank=True)
    FUNDCOUNT = models.IntegerField( null=True, blank=True)
    FUNDAMOUNT = models.IntegerField(null=True, blank=True)
    FUNDFEE = models.IntegerField(null=True, blank=True)
    NACCOUNT = models.IntegerField( null=True, blank=True)
    NACAMOUNT = models.IntegerField(null=True, blank=True)
    NACFEE = models.IntegerField( null=True, blank=True)
    CBCCOUNT = models.IntegerField( null=True, blank=True)
    CBCAMOUNT = models.IntegerField( null=True, blank=True)
    CBCFEE = models.IntegerField( null=True, blank=True)
    CBQCOUNT = models.IntegerField(null=True, blank=True)
    CBQAMOUNT = models.IntegerField(null=True, blank=True)
    CBQFEE = models.IntegerField(null=True, blank=True)
    SURCHARGEFEE = models.IntegerField( null=True, blank=True)
    BRANCHORDER = models.IntegerField( null=True, blank=True)
    ATMORDER = models.IntegerField( null=True, blank=True)
    ORDERNBR = models.IntegerField( null=True, blank=True)
    TRACENBR = models.IntegerField( null=True, blank=True)
    TRACEMSG = models.IntegerField( null=True, blank=True)
    TRACEDBMSG = models.IntegerField( null=True, blank=True)
    fee_cup = models.IntegerField(null=True, blank=True)
    fee_napas = models.IntegerField(default=0, null=True, blank=True)
    fee_return = models.IntegerField(null=True, blank=True, default=0)

    def __str__(self):
        if self.ATMNAME is None:
            return self.BRANCH
        return self.ATMNAME

class Summary02(models.Model):
    BRANCH = models.CharField(max_length=200)
    ATMNAME = models.CharField(max_length=100, blank=True, null=True)
    TERMINALID = models.CharField(max_length=10, blank=True, null=True)
    LOGNO = models.IntegerField(blank=True, null=True)
    ATMCOUNT = models.IntegerField(null=True, default= 0)
    ATMAMOUNT = models.IntegerField(null=True, default= 0)
    ATMFEE = models.IntegerField(null=True, default= 0)
    BALCOUNT = models.IntegerField(null=True, blank=True)
    BALFEE = models.IntegerField(null=True, blank=True)
    MINICOUNT = models.IntegerField(null=True, blank=True)
    MINIFEE = models.IntegerField( null=True, blank=True)
    FUNDCOUNT = models.IntegerField( null=True, blank=True)
    FUNDAMOUNT = models.IntegerField(null=True, blank=True)
    FUNDFEE = models.IntegerField(null=True, blank=True)
    NACCOUNT = models.IntegerField( null=True, blank=True)
    NACAMOUNT = models.IntegerField(null=True, blank=True)
    NACFEE = models.IntegerField( null=True, blank=True)
    CBCCOUNT = models.IntegerField( null=True, blank=True)
    CBCAMOUNT = models.IntegerField( null=True, blank=True)
    CBCFEE = models.IntegerField( null=True, blank=True)
    CBQCOUNT = models.IntegerField(null=True, blank=True)
    CBQAMOUNT = models.IntegerField(null=True, blank=True)
    CBQFEE = models.IntegerField(null=True, blank=True)
    SURCHARGEFEE = models.IntegerField( null=True, blank=True)
    BRANCHORDER = models.IntegerField( null=True, blank=True)
    ATMORDER = models.IntegerField( null=True, blank=True)
    ORDERNBR = models.IntegerField( null=True, blank=True)
    TRACENBR = models.IntegerField( null=True, blank=True)
    TRACEMSG = models.IntegerField( null=True, blank=True)
    TRACEDBMSG = models.IntegerField( null=True, blank=True)
    fee_sum_01 = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        if self.ATMNAME is None:
            return self.BRANCH
        return self.ATMNAME

class Summary03(models.Model):
    BRANCH = models.CharField(max_length=200)
    ATMNAME = models.CharField(max_length=100, blank=True, null=True)
    TERMINALID = models.CharField(max_length=10, blank=True, null=True)
    LOGNO = models.IntegerField(blank=True, null=True)
    ATMCOUNT = models.IntegerField(null=True, default= 0)
    ATMAMOUNT = models.IntegerField(null=True, default= 0)
    ATMFEE = models.IntegerField(null=True, default= 0)
    BALCOUNT = models.IntegerField(null=True, blank=True)
    BALFEE = models.IntegerField(null=True, blank=True)
    MINICOUNT = models.IntegerField(null=True, blank=True)
    MINIFEE = models.IntegerField( null=True, blank=True)
    FUNDCOUNT = models.IntegerField( null=True, blank=True)
    FUNDAMOUNT = models.IntegerField(null=True, blank=True)
    FUNDFEE = models.IntegerField(null=True, blank=True)
    NACCOUNT = models.IntegerField( null=True, blank=True)
    NACAMOUNT = models.IntegerField(null=True, blank=True)
    NACFEE = models.IntegerField( null=True, blank=True)
    CBCCOUNT = models.IntegerField( null=True, blank=True)
    CBCAMOUNT = models.IntegerField( null=True, blank=True)
    CBCFEE = models.IntegerField( null=True, blank=True)
    CBQCOUNT = models.IntegerField(null=True, blank=True)
    CBQAMOUNT = models.IntegerField(null=True, blank=True)
    CBQFEE = models.IntegerField(null=True, blank=True)
    SURCHARGEFEE = models.IntegerField( null=True, blank=True)
    BRANCHORDER = models.IntegerField( null=True, blank=True)
    ATMORDER = models.IntegerField( null=True, blank=True)
    ORDERNBR = models.IntegerField( null=True, blank=True)
    TRACENBR = models.IntegerField( null=True, blank=True)
    TRACEMSG = models.IntegerField( null=True, blank=True)
    TRACEDBMSG = models.IntegerField( null=True, blank=True)
    fee_sum_02 = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        if self.ATMNAME is None:
            return self.BRANCH
        return self.ATMNAME

class SummaryFee(models.Model):
    name_branch = models.CharField(max_length=100)
    code_branch = models.IntegerField()
    code_unit = models.CharField(max_length=200, null=True, blank=True)
    fee_atm = models.IntegerField()
    fee_surcharg = models.IntegerField()
    fee_napas = models.IntegerField()
    fee_sum = models.IntegerField()

    def __str__(self):
        return self.name_branch
    
class FeeCBC(models.Model):
    terminal_id = models.CharField(max_length=10, null=True, blank=True)
    fee_cbc = models.IntegerField(default=0)
    
    def __str__(self):
        return self.terminal_id
    
class FeeQR(models.Model):
    terminal_id = models.CharField(max_length=10, null=True, blank=True)
    fee_qr = models.IntegerField(default=0)
    
    def __str__(self):
        return self.terminal_id

class FeeCUP(models.Model):
    terminal_id = models.CharField(max_length=10, null=True, blank=True)
    fee_cup = models.IntegerField(default=0)

    def __str__(self):
        return self.terminal_id
    

class FeeADD(models.Model):
    code_produc = models.CharField(max_length=20, null=True, blank=True)
    name_produc = models.CharField(max_length=100, null=True, blank=True)
    fee_01 = models.IntegerField(null=True, blank=True)
    fee_02 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name_produc
    
class SummaryATM(models.Model):
    branch = models.CharField(max_length=200)
    atm_name = models.CharField(max_length=200)
    terminal_id = models.CharField(max_length=10)
    atm_sum = models.IntegerField(null=True, blank=True)
    surcharge_sum = models.IntegerField(null=True, blank=True)
    napas_sum = models.IntegerField(null=True, blank=True)
    fee_sum = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.atm_name
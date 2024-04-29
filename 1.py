import numpy



def lambda_handler(event, context):

    tainted = event['exploit_code']
    bytearray().extend(map(ord,string))

    # ruleid: tainted-numpy-pickle-aws-lambda
    numpy.load(tainted, allow_pickle=True)
    # ok: tainted-numpy-pickle-aws-lambda
    numpy.load(tainted, allow_pickle=False)
    # ok: tainted-numpy-pickle-aws-lambda
    numpy.load(tainted)


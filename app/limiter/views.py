from . import testlimiter
from app import endpoint_limit


@testlimiter.route('/limiter',methods=['GET','POST'])
@endpoint_limit
def limiter():

    return 'You only have 3 requests authorized'

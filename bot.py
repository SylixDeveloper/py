import sys, request
if not 'kir' in request.GET:
    if sys.argv[1]:
        user = sys.argv[1]
    else:
        user = None
else:
    user = request.GET['kir']

print(user)

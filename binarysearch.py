def binarysearch(x,mas,low,high)-> int:
    """x- number which we find 
       mas- the source we are looking for
       low- min border 
       high- max border"""
    if low>high:
        return False
    else:
        mid=(high+low)//2
        if mas[mid]==x:
            return mid

        elif x<mas[mid]:
            return binarysearch(x,low,mid-1,mas)
        else:
            return binarysearch(x,mid+1,high,mas)
# here you still need to add a function call
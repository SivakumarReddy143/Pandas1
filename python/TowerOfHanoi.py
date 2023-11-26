def TowerOfhanoi(n,source,auxiliary,destination):
    if(n==0):
        return
    TowerOfhanoi(n-1, source, destination, auxiliary)
    print("move disk",n,"from source",source,"to destination",destination)
    TowerOfhanoi(n-1, auxiliary, source, destination)
    # TowerOfhanoi(n-1, source, auxiliary, destination)
    # print("move disk",n,"from source ",source,"to destination",destination)
    # TowerOfhanoi(n-1, auxiliary, destination, source)
n=3
TowerOfhanoi(n, 'A', 'B', 'C')
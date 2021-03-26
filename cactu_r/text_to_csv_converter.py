import csv



#extracting data from from the .txt file on which the readings are redirected
with open("cactu_r.txt","r") as f:
	lines = f.read().strip().split('\n')
	arr = []
	for word in lines:
		arr.extend(word.strip().split(" "))
elems = [i for i in arr if i != '']
arr = []

# dictionary for storing values
store = {"L1-dcache-load-misses":[],"iTLB-load-misses":[],"L1-icache-load-misses":[],"LLC-store-misses":[],"branch-misses:u":[],"LLC-load-misses":[],"dTLB-load-misses":[],"dTLB-store-misses":[],"L2-load-misses":[],"L2-store-misses":[],"cycles":[],"instructions":[],"ns":[]}
set1 = set(["L1-dcache-load-misses","iTLB-load-misses","L1-icache-load-misses","LLC-store-misses","branch-misses:u","LLC-load-misses","dTLB-load-misses","dTLB-store-misses","L2-store-misses","L2-load-misses","cycles","instructions","ns"])
for i in range(len(elems)):
	if elems[i] in set1:
		store[elems[i]].append(elems[i-1])

#print(store)

#forwarding the data from .txt file to .csv file
with open("cactu_r_test.csv","w",newline ='') as f:
	thewriter = csv.writer(f)

	thewriter.writerow(["L1-dcache-load-misses","iTLB-load-misses","L1-icache-load-misses","LLC-store-misses","branch-misses:u","LLC-load-misses","dTLB-load-misses","dTLB-store-misses","L2-load-misses","L2-store-misses","cycles","instructions","ns"])

	sz = len(store["L1-dcache-load-misses"])
	print(sz)
	for i in range(sz):
		xd = []
		for cols in store:
			xd.append(store[cols][i])
		thewriter.writerow(xd)

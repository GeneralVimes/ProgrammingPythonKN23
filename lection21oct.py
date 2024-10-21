#наївний алгоритм пошуку всіх дільгників числа N
def find_all_divisors_var1(N):
	res=[]
	d=1
	while d<=N:#тому що на блок-схемі гілки від ромба зацклені
		if N%d==0:#тому що на блок-схемі гілки йдуть вниз
			res.append(d)
		d=d+1
	return res

print(find_all_divisors_var1(6))
print(find_all_divisors_var1(72))
int pow1(int n){
	int p=1;
	for(int i=1; i<=n; i++){
		p*=2;
	}
	return p;
}

int pow2(int n){
	return (n==0)? 1: 2*pow2(n-1);
}

public class IntList {
	public int first;
	public IntList rest;

	public IntList(int f,IntList r){

		first = f;
		rest = r;
	}

	public int size(){

		if (rest == null){
			return 1;
		}
		else{

			return 1+ this.rest.size();
		}
	}


    public int iterativeSize(){

    	IntList p = this;
    	int totalSize = 0;
    	while(p!=null){

    		totalSize += 1;
    		p = p.rest;
    	}
    	return totalSize;
    }	
    

    public int get(int number){
    	// IntList p = this;
    	// int i = 0;
    	// while(true ){
    	// 	if(i < number){
    	// 		i += 1;
    	// 		p=p.rest;
    	// 	}
    	// 	else{
     //            return p.first;
    	// 	}
    	// }

    	if number == 0{
    		return first
    	}
    	else{
    		return rest.get(i-1)
    	}
    }
	public static void main(String[] args) {

    IntList L = new IntList(5,null);
    L = new IntList(10,L);
    L = new IntList(15,L);
    System.out.println(L.get(0));
	}
	
}
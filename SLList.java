// the SLList is a IntNode package,the addFirst,getFirst is designed
public class SLList{

	// static means that methods inside the static class can not access any of the members of the enclosing class

	    public static class IntNode{
	        public int item;
	        public IntNode next;
	        public IntNode(int i,IntNode n){
                item = i;
                next = n;
	        }
         }
    private IntNode sentinel;
    private IntNode first;

    private int size;


	// public SLList(int x){
	//     first = new IntNode(x,null);
	//     size = 1;
	// }


	// create null list
	public SLList(){
		first = null;
		sentinel = null;
		size = 0;
	}
    

    // public void addLast(int x){
    // 	IntNode p = first;
    // 	while(p.next != null){
    // 		p = p.next;
    // 	}
    // 	p.next = new IntNode(x,null);
    // }
    
    // public void addLast(int x){
    // 	size += 1;
    	
    // 	if (first == null) {
    // 		first = new IntNode(x,null);
    // 		return
    // 	}

    // 	while (p.next != null){
    // 		p = p.next;
    // 	}
    // 	p.next = new IntNode(x,null);
    	
    // }


    // add sentinel node
    public void addLast(int x){
    	size += 1; 
    	
    	IntNode p = sentinel;
        while (p.next != null) {
            p = p.next;
        }

        p.next = new IntNode(x, null);
    	
    }


	public void addFirst(int x){
		first = new IntNode(x,first);
		sentinel = first;
		size += 1;
	}


	public int getFirst(){
		return first.item;
	}


	private int size(IntNode p){
		// if (p.next == null){
		// 	return 1;
		// }
		// else
		// 	return 1 + size(p.next);
		return size;
	}


    public int size(){
    	return size(first);
    }
    

    public static void main(String[] args){
    	SLList L = new SLList();
    	L.addFirst(20);
    	
        L.addLast(3);
        L.addFirst(10);
        // L.addLast(3);
        System.out.println(L.size());
        System.out.println(L.getFirst());
    }
}


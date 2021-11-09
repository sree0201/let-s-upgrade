class Test{
    public static void main(String[] args){
        System.out.println("Hello");
        System.out.println("Coders");   
    }    
}
class Iphone{
    int contact;
    void showData(){
        System.out.println("Subbu's No - " + contact);
    }
    public static void main(String[] args){
        Iphone ob = new Iphone();
        ob.contact = 83389;
        ob.showData();
    }
}

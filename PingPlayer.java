package py4j;
import py4j.GatewayServer;
public class PingPlayer 
{
   
    public int multi(int a)
    { return a*2;
    }
    public int divi(int b)
    {
        return b/2;
    }


     public static void main(String[] args) {
        PingPlayer y=new PingPlayer();
        GatewayServer gatewayServer = new GatewayServer(y);
        gatewayServer.start();
        System.out.println("Gateway Server Started");
    }

}

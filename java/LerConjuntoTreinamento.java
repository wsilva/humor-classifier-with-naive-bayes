import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.File;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;
import java.util.Hashtable;


public class LerConjuntoTreinamento{



  public static void main (String [] args){
    String arqTreinamento = "Sentiment Analysis Dataset.csv";
    BufferedReader br = null;
    String linha = "";
    Map<String,String> dados = new HashMap<String,String>();
    int numDoc = 0;
    int probPositiva = 0, probNegativa = 0, numClassePositiva=0, numClasseNegativa=0;

    try {

      br = new BufferedReader(new FileReader(arqTreinamento));

      while ((linha = br.readLine()) != null) {

        String[] twit = linha.split(",");
        twit[0] = twit[0].replaceAll("[^0-9 ]", "");
        twit[3] = twit[3].replaceAll("[^a-zA-Z ]", "");
        twit[3] = twit[3].toLowerCase();
        //Colocando no HashMap - chave = msg valor = sentimento
        dados.put( twit[3], twit[1]);

        numDoc++;
        if(Integer.parseInt(twit[1]) == 1)numClassePositiva++;
        else numClasseNegativa++;

        //if(Integer.parseInt(twit[0])<= 5000)System.out.println(twit[0] + "Sentimento  " + twit[3] + "    Mensagem " + dados.get(twit[3]));
      }

    } catch (FileNotFoundException e) {
        e.printStackTrace();
    } catch (IOException e) {
        e.printStackTrace();
    } finally {
        if (br != null) {
          try {
              br.close();
          } catch (IOException e) {
              e.printStackTrace();
          }
        }
    }


    //probabilidade das classes numDoc = nºlinhas
    probPositiva = numClassePositiva/numDoc;
    probNegativa= numClasseNegativa/numDoc;

    System.out.println("pos " + probPositiva + "  neg " +probNegativa);

    //Colocando as palavras na hashTable
    Hashtable<String, Integer> vocabulario = new Hashtable<String, Integer>();





  }
}
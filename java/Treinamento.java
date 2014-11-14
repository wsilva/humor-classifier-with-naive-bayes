package ia;

public class Treinamento {
	//caracteristicas do problema tweets
    private int ItemID;
    private String Sentimento;
    private String SentimentoSource;
    private String SentimentoTexto;

    //construtor
    public Treinamento(int ItemID, String Sentimento, String SentimentoSource, String SentimentoTexto){

        this.ItemID = ItemID;
        this.Sentimento = Sentimento;
        this.SentimentoSource = SentimentoSource;
        this.SentimentoTexto = SentimentoTexto;
        
    }
    //gets e sets
    public int getItemID() {
        return ItemID;
    }

    public void setItemID(int item) {
        this.ItemID = item;
    }

    public String getSentimento() {
        return Sentimento;
    }

    public void setSentimento(String sent) {
        this.Sentimento = sent;
    }

    public String getSentimentoSource() {
        return SentimentoSource;
    }

    public void setSentimentoSource(String sentSource) {
        this.SentimentoSource = sentSource;
    }

    public String geSentimentoTexto() {
        return SentimentoTexto;
    }

    public void setSentimentoTexto(String sentTexto) {
        this.SentimentoTexto =  sentTexto;
    }

    //metodo para calcular o numero de classes passada nele    
    public double calculaQuantidadeClasse(Treinamento[] arrayTreinamento, String sentimetoDeClasse){

        double calcula = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){

            if(sentimetoDeClasse.equals(arrayTreinamento[i].getSentimento())){
            	calcula++;

            }

    }
        return calcula;

    }


}

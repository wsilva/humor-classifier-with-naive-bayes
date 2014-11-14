package ia;

public class NaiveBayes {
	//calcular a probabilidade a priori das classes
    public double probabilidadePrioriClasse(Treinamento[] arrayTreinamento, String sentimetoDeClasse){

        int cont = 0;
        double probPrioriClasse = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){
            if(sentimetoDeClasse.equals(arrayTreinamento[i].getSentimento())){

                cont++;
        }
            probPrioriClasse = cont/(double)arrayTreinamento.length;

        }

        return probPrioriClasse;

    }

    //calcular a probabilidade dos valores das caracteristicas de SentimentoSource
    public double probabilidadeCaracteristicaSentimentoSource(Treinamento[] arrayTreinamento, String classificacao){

        int cont = 0;
        double probabilidadeCaracteristicaSentimentoSource = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){
            if(classificacao.equals(arrayTreinamento[i].getSentimentoSource())){

                cont = cont + 1;
        }
            probabilidadeCaracteristicaSentimentoSource = cont/(double)arrayTreinamento.length;

        }

        return probabilidadeCaracteristicaSentimentoSource;

    }

    //calcular a probabilidade dos valores das caracteristicas de SentimentoTexto
    public double probabilidadeCaracteristicaSentimentoTexto(Treinamento[] arrayTreinamento, String classificacao){

        int cont = 0;
        double probabilidadeCaracteristicaSentimentoTexto = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){
            if(classificacao.equals(arrayTreinamento[i].geSentimentoTexto())){

                cont = cont + 1;
        }
            probabilidadeCaracteristicaSentimentoTexto = cont/(double)arrayTreinamento.length;

        }

        return probabilidadeCaracteristicaSentimentoTexto;

    }

    

    //calcular a probabilidade condicional entre os valores das caracteristicas de  SentimentoSource e as classes
    public double probabilidadeCondicionalClasseCaracteristicaSentimentoSource(Treinamento[] arrayTreinamento, String classificacao, String sentimetoDeClasse){

        int cont = 0;
        double probabilidadeCondicionalClasseClassificacaoSentimentoSource = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){
            if(sentimetoDeClasse.equals(arrayTreinamento[i]. getSentimento()) && classificacao.equals(arrayTreinamento[i].getSentimentoSource())){
                cont++;

            }

            probabilidadeCondicionalClasseClassificacaoSentimentoSource = cont/arrayTreinamento[0].calculaQuantidadeClasse(arrayTreinamento, sentimetoDeClasse);
        }


        return probabilidadeCondicionalClasseClassificacaoSentimentoSource;

    }

    //calcular a probabilidade condicional entre os valores das caracteristicas de SentimentoTexto e as classes
    public double probabilidadeCondicionalClasseCaracteristicaSentimentoTexto(Treinamento[] arrayTreinamento, String classificacao, String sentimetoDeClasse){

        int cont = 0;
        double probabilidadeCondicionalClasseClassificacaoSentimentoTexto = 0.0;

        for(int i=0; i<arrayTreinamento.length; i++){
            if(sentimetoDeClasse.equals(arrayTreinamento[i]. getSentimento()) && classificacao.equals(arrayTreinamento[i].getSentimentoSource())){
                cont++;

            }

            probabilidadeCondicionalClasseClassificacaoSentimentoTexto = cont/arrayTreinamento[0].calculaQuantidadeClasse(arrayTreinamento, sentimetoDeClasse);
        }


        return probabilidadeCondicionalClasseClassificacaoSentimentoTexto;
    }

    //calcular a probabilidade a posteriori entre os valores das caracteristicas de SentimentoSource e as classes
    public double probabilidadePosterioriClasseCaracteristicaSentimentoSource( Treinamento[] arrayTreinamento, String classificacao, String sentimetoDeClasse){
         double resultadoProbabilidadeCondicionalClasseCaracteristicaSentimentoSource  = this.probabilidadeCondicionalClasseCaracteristicaSentimentoSource(arrayTreinamento, classificacao,sentimetoDeClasse);
         double resultadoProbabilidadeCaracteristicaSentimentoSource  = this.probabilidadeCaracteristicaSentimentoSource(arrayTreinamento,classificacao);
         double resultadoProbabilidadePrioriClasse = this.probabilidadePrioriClasse(arrayTreinamento,sentimetoDeClasse);
         
         double resultadoFinal = (resultadoProbabilidadeCondicionalClasseCaracteristicaSentimentoSource * resultadoProbabilidadePrioriClasse)/resultadoProbabilidadeCaracteristicaSentimentoSource;


        return resultadoFinal;

    }

    //calcular a probabilidade a posteriori entre os valores das caracteristicas de SentimentoTexto e as classes
    public double probabilidadePosterioriClasseCaracteristicaSentimentoTexto( Treinamento[] arrayTreinamento, String classificacao, String sentimetoDeClasse){
         double resultadoProbabilidadeCondicionalClasseCaracteristicaSentimentoTexto = this.probabilidadeCondicionalClasseCaracteristicaSentimentoTexto(arrayTreinamento, classificacao, sentimetoDeClasse);
         double resultadoProbabilidadeCaracteristicaSentimentoTexto = this.probabilidadeCaracteristicaSentimentoTexto(arrayTreinamento, classificacao);
         double resultadoProbabilidadePrioriClasse = this.probabilidadePrioriClasse(arrayTreinamento, sentimetoDeClasse);
         double resultadoFinal = (resultadoProbabilidadeCondicionalClasseCaracteristicaSentimentoTexto * resultadoProbabilidadePrioriClasse)/resultadoProbabilidadeCaracteristicaSentimentoTexto;
         return resultadoFinal;
    }

    /*Classificador
    public double classificadorNaiveBayesSentimentoPositivo(String caracteristicaSentimentoSource, String caracteristicaSentimentoTexto, ResultadosTreinamento resultado){
        double classif1 = 0.0;
        double classif2 = 0.0;
        if(caracteristicaSentimentoSource.equals("Sentiment140")){
        	classif1 = resultado.getResultadoPosterioriSentimentoPositivo();

        return (classif1 * classif2);

    }


    Classificador
    public double classificadorNaiveBayesSentimentoNegativo(String  caracteristicaSentimentoSource, String caracteristicaSentimentoTexto, ResultadosTreinamento resultado){
        double classif1 = 0.0;
        double classif2 = 0.0;

        if(caracteristicaSentimentoSource.equals("Sentiment140")){
        	classif1 = resultado.getResultadoPosterioriSentimentoNegativo();


        return (classif1 * classif2);

    }*/

}

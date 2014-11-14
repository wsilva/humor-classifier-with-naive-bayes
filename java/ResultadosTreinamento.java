package ia;

public class ResultadosTreinamento {
	 private double ResultadoPosterioriSentimentoPositivo= 0.0;
	    private double ResultadoPosterioriSentimentoNegativo= 0.0;
	    
	    public ResultadosTreinamento() {
	    }

	    public double getResultadoPosterioriSentimentoPositivo() {
	        return ResultadoPosterioriSentimentoPositivo;
	    }

	    public void setResultadoPosterioriSentimentoPositivo(double positivo) {
	        this.ResultadoPosterioriSentimentoPositivo = positivo;
	    }

	    public double getResultadoPosterioriSentimentoNegativo() {
	        return ResultadoPosterioriSentimentoNegativo;
	    }

	    public void setResultadoPosterioriSentimentoNegativo(double negativo) {
	        this.ResultadoPosterioriSentimentoNegativo = negativo;
	    }
}

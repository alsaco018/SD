/*****************************************************************************
Alberto Saldanna Contreras
David Naranjo Vieytes
Universidad de C�diz (Spain)
*****************************************************************************/

package eventos;

import org.python.modules.math;

public class EventoOla {    
    
    private float temperatura;
    private String sensor;
    private float presion;
    private float velocidadViento;
    private float direccionViento;
    private float sensacionTermica;
    private float alturaMaxOla;
    private float alturaMinOla;
    private float periodo;
    private boolean ingles = true;
    
    public EventoOla(float t, String s, float p, float velVi, float dirV, float alMx, float alMn, float sen, float per, boolean ing) {
        temperatura = t;
        sensor = s;  
        presion = p;
        velocidadViento = velVi;
        direccionViento = dirV;
        alturaMaxOla = alMx;
        alturaMinOla = alMn;
        sensacionTermica = sen;
        periodo = per;
        ingles = ing;
        
    }
        
    public EventoOla() {
        
    }
    
public String getTweetIngles(){
    	
    	String recomendacion="None";
    	
    	double valoracion = ((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)*3.5;
    	
    	if(45 <Math.abs(this.getDireccionViento())&& Math.abs(this.getDireccionViento())< 135){
    		
    		if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)<=1.5 && 15<this.getVelocidadViento()){
    			
    			recomendacion = "Perfect day to learn.";
    			valoracion += 2;
    			
    			
    		}else if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)>1.5 && 23>this.getVelocidadViento()){
    			
    			recomendacion = "Perfect day, let's surf!.";
    			valoracion += 2;
    			
    		}else if(this.getAlturaMaxOla()>2.8){
    			
    			valoracion -=2;
    			recomendacion = "Don't surf, it's dangerous.";
    			
    		}
    		
    	}else if(225 <Math.abs(this.getDireccionViento())&& Math.abs(this.getDireccionViento())< 315){
    		
    		if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)<=1.5 && 0.8<this.getVelocidadViento()){
    			
    			recomendacion = "Perfect day to learn.";
    			valoracion += 2;
    			
    			
    		}else if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)>1.5 && 15>this.getVelocidadViento()){
    			
    			recomendacion = "Perfect day, let's surf!.";
    			valoracion += 2;
    			
    		}else if(this.getAlturaMaxOla()>2.8){
    			
    			valoracion -=2;
    			recomendacion = "Don't surf, it's dangerous.";
    			
    		}
    	}else{
    		valoracion +=1;
    	}
    	
    	if(17< this.getSensacionTermica() && this.getSensacionTermica()<30){
    		valoracion +=0.8;
    	}
    	
    	if(this.getPeriodo()>=10) valoracion+=1;
    	
    	return "Data for next 3h (Cádiz): "+"\n"
    			+ "-Max wave's height: "+this.getAlturaMaxOla()+
    			"\n-Min wave's height: "+this.getAlturaMinOla()+
    			"\n-Wave periode: "+this.getPeriodo()+
    			"\n-VWind speed (Km/h): "+this.getVelocidadViento()+
    			"\n-Wind direction: "+this.getDireccionViento()+"º"+
    			"\n-Apparent air temperature: "+this.getSensacionTermica()+" Cº"+
    			"\n\n*Rate = "+valoracion+"/10"+
    			"\n *Recomendation: "+recomendacion;

    	
    	
    }
    
public String getTweet(){
    	
    	String recomendacion="Ninguna";
    	
    	double valoracion = ((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)*3.5;
    	
    	if(45 <Math.abs(this.getDireccionViento())&& Math.abs(this.getDireccionViento())< 135){
    		
    		if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)<=1.5 && 15<this.getVelocidadViento()){
    			
    			recomendacion = "Dia perfecto para aprender.";
    			valoracion += 2;
    			
    			
    		}else if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)>1.5 && 23>this.getVelocidadViento()){
    			
    			recomendacion = "Dia perfecto para surfear.";
    			valoracion += 2;
    			
    		}else if(this.getAlturaMaxOla()>2.8){
    			
    			valoracion -=2;
    			recomendacion = "No surfear, el oleaje es peligroso.";
    			
    		}
    		
    	}else if(225 <Math.abs(this.getDireccionViento())&& Math.abs(this.getDireccionViento())< 315){
    		
    		if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)<=1.5 && 0.8<this.getVelocidadViento()){
    			
    			recomendacion = "Dia perfecto para aprender.";
    			valoracion += 2;
    			
    			
    		}else if(((this.getAlturaMaxOla()+this.getAlturaMinOla())/2)>1.5 && 15>this.getVelocidadViento()){
    			
    			recomendacion = "Dia perfecto para surfear.";
    			valoracion += 2;
    			
    		}else if(this.getAlturaMaxOla()>2.8){
    			
    			valoracion -=2;
    			recomendacion = "No surfear, el oleaje es peligroso.";
    			
    		}
    	}else{
    		valoracion +=1;
    	}
    	
    	if(17< this.getSensacionTermica() && this.getSensacionTermica()<30){
    		valoracion +=0.8;
    	}
    	
    	if(this.getPeriodo()>=10) valoracion+=1;
    	
    	return "Datos del oleaje en la próximas 3h (Cádiz): "+"\n"
    			+ "-Altura max de la ola: "+this.getAlturaMaxOla()+
    			"m\n-Altura min de la ola: "+this.getAlturaMinOla()+
    			"m\n-Periodo de la ola: "+this.getPeriodo()+
    			"s\n-Velocidad del viento (Km/h): "+this.getVelocidadViento()+
    			"\n-Direccion del viento: "+this.getDireccionViento()+"º"+
    			"\n-Sensacion termica: "+this.getSensacionTermica()+" Cº"+
    			"\n\n*Puntuacion = "+valoracion+"/10"+
    			"\n *Recomendacion: "+recomendacion;

    	
    	
    }

	public float getPeriodo(){
		return periodo;
	}
	
	public boolean getIngles(){
		return ingles;
	}

    public float getTemperatura() {
        return temperatura;
    }
    
    public String getSensor() {
        return sensor;
    }
    public float getPresion(){
        return presion;
    }

    public float getVelocidadViento() {
        return velocidadViento;
    }

    public float getDireccionViento() {
        return direccionViento;
    }
    
    
    public float getAlturaMaxOla(){
        return alturaMaxOla;
    }
    
    public float getAlturaMinOla(){
        return alturaMinOla;
    }
    
    public float getSensacionTermica(){
        return sensacionTermica;
    }
    
    public void setTemperatura(float t) {
        
        temperatura = t;
    }
    
    public void setIngles(boolean i){
    	ingles = !i;
    }

    public void setSensor(String s) {
        sensor = s;
    }
    
    public void setPresion(float p){
        presion = p;
    }

    public void setVelocidadViento(float vel) {
        
        velocidadViento = vel;
    }

    public void setPeriodo(float per){
    	periodo = per;
    }
    
    public void setDireccionViento(float dir){
        direccionViento = dir;
    }
    
    public void setAlturaOlaMin(float alMin) {
        alturaMinOla = alMin;
        
    }
    
    public void setAlturaOlaMax(float alMax) {
        alturaMaxOla = alMax;
        
    }
    
    public void setSensacionTermica(){
        sensacionTermica = calcularSensacionTermica(velocidadViento, temperatura);
    }
    public float calcularSensacionTermica(float vel, float t){
        //(13.12 + (0.6215 * t) - (11.37 * vel)* 0.16 + (0.3965 * (vel * t)) * 0.16)
        return (float) (33 + (t - 33)*(0.474 + 0.454 * math.sqrt((vel * 0.6214)* 0.447) - 0.0454 * (vel * 0.6214)* 0.447));
    }

    @Override
    public String toString() {
        return "Datos para las proximas 3 hora:\n - Localidad = " + sensor
                + "\n - Temperatura:  " + temperatura
                + " ºC\n - Sensacion termica = " + sensacionTermica
                + " ºC\n - Velocidad del viento = " + velocidadViento
                + " km/h\n - Direccion del viento = " + direccionViento
                + " º\n - Presion = " + presion
                + " mb\n - Altura maxima de ola = " + alturaMaxOla
                + " m\n - Altura minima de ola = " + alturaMinOla
                + " m\n - periodo = "+ periodo;
                
    }

    
}

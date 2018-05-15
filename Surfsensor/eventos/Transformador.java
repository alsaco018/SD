package eventos;

import java.util.Date;


import org.mule.api.annotations.ContainsTransformerMethods;
import org.mule.api.annotations.Transformer;
import org.mule.module.json.JsonData;



//import eventos.EventoHogar;
import eventos.EventoOla;

// ver http://www.mulesoft.org/docs/site/current3/apidocs/org/mule/module/json/JsonData.html


@ContainsTransformerMethods
public class Transformador
{
    
    @Transformer  
    public EventoOla JSONToEventoOla(JsonData obj) throws Exception
    {            
        EventoOla evento = new EventoOla();
        String nombreSensor = "Cadiz";
        Date actual = new Date(System.currentTimeMillis());
        
        for(int i = 0; i < 8; ++i){
            String istr = Integer.toString(i);
            istr = istr.concat("]");
            String llamada = "[";
            llamada = llamada.concat(istr);
            String istrAnt = Integer.toString(i-1);
            istrAnt = istrAnt.concat("]");
            String llamadaAnt = "[";
            llamadaAnt = llamadaAnt.concat(istrAnt);
            
            
            long timestamp = Long.parseLong(obj.getAsString(llamada.concat("/localTimestamp")));
            Date hora = new Date(timestamp * 1000);
            boolean noEncontrado = true;
            
            if(actual.before(hora) && noEncontrado) {
                evento.setTemperatura(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/condition/temperature"))));
                evento.setSensor(nombreSensor);
                evento.setPresion(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/condition/pressure"))));
                evento.setVelocidadViento(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/wind/speed"))));
                evento.setDireccionViento(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/wind/direction"))));
                evento.setAlturaOlaMax(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/swell/absMaxBreakingHeight"))));
                evento.setAlturaOlaMin(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/swell/absMinBreakingHeight"))));
                evento.setPeriodo(Float.parseFloat(obj.getAsString(llamadaAnt.concat("/swell/components/combined/period"))));
                evento.setSensacionTermica();
                evento.setIngles(evento.getIngles());
                noEncontrado = false;
            }
        }
        return evento;
    }
}


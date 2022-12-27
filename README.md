# Situational Context  

## Note  
Going to keep it simple for now, will increase complexity later. Worry strictly about usage/rate of change of volume

### Environment  
Oxygen gas in a hospital.  

### System Diagram  
![System Diagram](system_diagram.png)

### Gas Demand
`5 000 000 Litres / day`. Random estimate. Will need to simulate load for accuracy.

Avg LPM calculation, based on one day's demand: `5000000 L/D / (24 h/d * 60 m/h) = 3472.22222 L/min`  

### Storage  
For initial development, assume simple configuration of a single, compressed gas-filled vessel. 

The vessel has a `10,000` L capacity, assume for now 100% pure oxygen.

Final product should support liquid storage vessel and cylinder manifold system. 

### Measurement  
Since inside of the tank is air in our idealized environment, we're using a pressure sensor. 

## CSA Standards
1. CSA [1, pg. 82] says that, for Oxygen supply:
- **Nominal Pressure:** 345 +35/-0 kPa
- **Typical Flows at Standard T (0 c) and P (100 kPa):**
  - Ventilator: 25 L/min 
  - Flowmeter: 2-10 L/min
  - Blender: 5-10 L/min
  - **Outlet Max: 25 L/min**

2. Low pressure is anything less than 1380 kPa (200 psi). ASSUMPTION: everything including or above 1380 kPa (200 psi) is high pressure.


# Sources
Saudi Journal of Anaesthesia [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8477771/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8477771/)

On liquid oxygen systems: https://pib.gov.in/PressReleasePage.aspx?PRID=1716197 

On ventilators: https://www.lhsc.on.ca/critical-care-trauma-centre/mechanical-ventilator 

On hospital oxygen gas systems: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8680427/ 

[1] CSA standard on medical gases: https://www.csagroup.org/store/product/Z7396.1-17/  

# Meta  
## Eventual Load Simulation   
Will need to simulate actual hospital usage eventually. 
#ifndef _NEURON_CPP
#define _NEURON_CPP

#include "iostream"

#include "neuron.h"

#include "math.h"

extern int SENSOR_NEURON;

extern int BIAS_NEURON;

extern int TANH_TRANSFER_FUNCTION;

NEURON::NEURON(int myID, int neuronType, int layer, double tau, int transferFunction) {

	Initialize(myID,neuronType,layer,tau,transferFunction);

	if ( type == BIAS_NEURON )

		value = 1.0;
}

NEURON::NEURON(int myID, int neuronType, int svIndex, int layer, double tau) {

	Initialize(myID,neuronType,layer,tau,TANH_TRANSFER_FUNCTION);
	
	sensorValueIndex = svIndex;
}

NEURON::~NEURON(void) {

}

int  NEURON::Get_ID(void) {

	return ID;
}

int  NEURON::Get_Layer(void) {

	return layer;
}

int  NEURON::Get_Sensor_Value_Index(void) {

	if ( Get_Type() != SENSOR_NEURON ) 

		return 0;

	else
		return sensorValueIndex;
}

int  NEURON::Get_Type(void) {

	return type;
}

double NEURON::Get_Previous_Value(void) {

	return previousValue;
}

double NEURON::Get_Tau(void) {

	return tau;
}

double NEURON::Get_Value(void) {

	return value;
}

void NEURON::Print(void) {

	std::cerr << ID << " ";

        std::cerr << type << " ";

        std::cerr << sensorValueIndex << " ";

        std::cerr << value << "\n";
}

void NEURON::Push_Current_Value_To_Previous_Value(void) {

	previousValue = value;
}

void NEURON::Reset(void) {

	value = 0.0;
}

void NEURON::Set(double v) {

	value = v;
}

void NEURON::Threshold(void) {

	if ( Get_Type() == SENSOR_NEURON )

		return;

	if ( transferFunction == TANH_TRANSFER_FUNCTION )

		value = tanh(value);

	// Otherwise, it is the identity function and nothing needs to be done.
}

// ------------------ Private methods -------------------

void NEURON::Initialize(int myID, int neuronType, int l, double t, int tr) {

        ID = myID;

        type = neuronType;

        sensorValueIndex = -1;

	layer = l;

	tau = t;

	transferFunction = tr;

        value = 0.0;

	previousValue = 0.0;

}

#endif

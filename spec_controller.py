from seabreeze.spectrometers import list_devices, Spectrometer
import datetime as dt
from seabreeze.spectrometers import list_devices, Spectrometer

class oceanoptic_controller():
    def __init__(self, integration = 100000, model = 'HR2000PLUS'):
        '''
        init the class 

        Parameters
        -----------
        init_time - integration time of the spectrometer, 

        model - model of the spectrometer

        Returns
        --------
        None
        '''
        self.integration_time = integration
        self.model = model
        self.status = False
        self.wl = []
        self.intens = []
        self.spec = []
        return
    
    def init_spec(self):
        '''
        loads the dll to the controller and initializes the dll using model name to find correct ocean optics spectr.

        Parameters
        -----------

        Returns
        --------
        None
        '''
        devices = list_devices()
        if len(devices) == 0:
            self.status = False
        else:
            # self.spec = Spectrometer.from_first_available()
            # self.spec.integration_time_micros(self.integration_time)
            # self.status = True
            i = 0
            for device in devices:
                if device.model == self.model:
                    break
                i += 1
            
     
            self.spec = Spectrometer.from_serial_number(devices[i].serial_number)
            self.spec.integration_time_micros(self.integration_time)
            self.status = True            
        return 


    def get_spectra(self):
        
        if not self.status:
            print("Ocean optics device not found attempting to find ")
            self.init_spec()
        else:
            self.wl = self.spec.wavelengths()
            self.intens = self.spec.intensities()


            # plt.title(" reflection")
            # plt.plot(self.wl, self.intens)
            # plt.xlabel("Wavelength [nm]")
            # plt.ylabel("Intensity [a.u.]")
            # plt.grid(True)
            # plt.show()
            
    def quit(self):
        self.spec.close()

# test = oceanoptic_controller(integration = 212000,model='HR2000PLUS')


# test.init_spec()

# # test.get_spectra()
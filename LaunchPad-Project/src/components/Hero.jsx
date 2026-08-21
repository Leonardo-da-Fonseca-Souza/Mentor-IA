import React from 'react';

export default function Hero() {
  return (
    <section className="relative min-h-[921px] flex items-center justify-center px-margin-mobile md:px-margin-desktop py-20 overflow-hidden">
      {/* Background Elements */}
      <div className="absolute inset-0 z-0">
        <div 
          className="w-full h-full bg-cover bg-center opacity-30 mix-blend-screen"
          style={{ backgroundImage: `url('https://lh3.googleusercontent.com/aida-public/AB6AXuDZyIsmjZlXRG4BNv8madP_ea57Xdkie5kThYQ6JExMTkN8hp0xfqM89vW7kG9TAPRsb7skfrGI0F-drPErGgD7A7HX0zSHujaITQUP-EfU7NG9iRvloXsJUe5Y00lqa9BP43WeMft0qXMSyrVQtQL1Zch-HXq2NIgVj6n_NhlbVAUDHAzppNu32dcBAEOMWygDON-7adIjRWseXWQQwhJT_x9L-ttT4_X9-DHzxmoLpHKMtjbKxl31')` }}
          aria-label="A sprawling, high-tech orbital space station orbiting Earth"
        ></div>
        <div className="absolute inset-0 bg-gradient-to-t from-background via-background/80 to-transparent"></div>
      </div>

      <div className="relative z-10 max-w-container-max mx-auto text-center space-y-8 mt-12">
        <span className="inline-block px-4 py-1 rounded-full glass-panel border-primary/30 text-primary font-label-caps uppercase tracking-widest text-label-caps mb-4">
          <span className="inline-block w-2 h-2 rounded-full bg-primary animate-pulse mr-2"></span>
          SISTEMAS ONLINE
        </span>
        
        <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-surface max-w-4xl mx-auto drop-shadow-2xl">
          O Futuro da <span className="text-transparent bg-clip-text bg-gradient-to-r from-primary to-secondary">Logística Espacial</span>
        </h1>
        
        <p className="font-body-lg text-body-lg text-tertiary max-w-2xl mx-auto">
          Sistemas de transporte orbital e telemetria de próxima geração projetados para as missões mais ousadas do sistema solar. Garanta a jornada da sua carga hoje.
        </p>
        
        <div className="flex flex-col sm:flex-row gap-4 justify-center items-center pt-8">
          <button className="w-full sm:w-auto px-8 py-4 bg-primary-container text-on-primary-container rounded-lg font-mono-label text-mono-label shadow-[0_0_20px_rgba(188,19,254,0.3)] hover:shadow-[0_0_30px_rgba(188,19,254,0.6)] transition-all duration-300 transform hover:-translate-y-1">
            Começar
          </button>
          <button className="w-full sm:w-auto px-8 py-4 bg-transparent border border-secondary text-secondary rounded-lg font-mono-label text-mono-label hover:bg-secondary/10 transition-all duration-300">
            Ver Telemetria <span className="material-symbols-outlined align-middle ml-2 text-sm">arrow_forward</span>
          </button>
        </div>
      </div>
    </section>
  );
}

import React from 'react';

export default function Features() {
  const featuresList = [
    {
      title: 'Manobra Orbital',
      description: 'Sistemas de propulsão avançados que oferecem precisão submilimétrica para acoplamentos complexos e ajustes de trajetória na órbita terrestre baixa.',
      icon: 'rocket_launch',
      colorClass: 'text-primary bg-primary/10',
    },
    {
      title: 'Segurança de Carga',
      description: 'Blindagem contra radiação de nível militar e regulação térmica garantindo o transporte sem degradação de instrumentação sensível.',
      icon: 'shield',
      colorClass: 'text-secondary bg-secondary/10',
      activeGlow: true,
    },
    {
      title: 'Telemetria em Tempo Real',
      description: 'Links de dados criptografados por quantum contínuos fornecendo dados estruturais e posicionais instantâneos em toda a rede orbital.',
      icon: 'radar',
      colorClass: 'text-primary bg-primary/10',
    },
  ];

  return (
    <section id="tech" className="py-32 px-margin-mobile md:px-margin-desktop relative z-10 bg-surface-dim">
      <div className="max-w-container-max mx-auto">
        <div className="text-center mb-16 space-y-4">
          <h2 className="font-headline-lg text-headline-lg text-on-surface">Tecnologias Principais</h2>
          <p className="font-body-md text-body-md text-tertiary max-w-2xl mx-auto">
            Engenharia de precisão e resiliência nos ambientes mais severos conhecidos pela humanidade.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
          {featuresList.map((feature, idx) => (
            <div 
              key={idx} 
              className={`glass-panel rounded-xl p-8 hover:bg-white/5 transition-colors duration-300 group ${feature.activeGlow ? 'glow-border-active relative overflow-hidden' : ''}`}
            >
              <div className={`w-12 h-12 rounded-full flex items-center justify-center mb-6 group-hover:scale-110 transition-transform ${feature.colorClass}`}>
                <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>
                  {feature.icon}
                </span>
              </div>
              <h3 className="font-headline-md text-headline-md text-on-surface mb-3 text-xl">
                {feature.title}
              </h3>
              <p className="font-body-md text-body-md text-tertiary">
                {feature.description}
              </p>
              {feature.activeGlow && (
                <div className="absolute -bottom-10 -right-10 w-32 h-32 bg-secondary/20 blur-[50px] rounded-full pointer-events-none"></div>
              )}
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

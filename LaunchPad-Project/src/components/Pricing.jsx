import React from 'react';

export default function Pricing() {
  const tiers = [
    {
      name: 'Suborbital',
      price: '$2.5M',
      period: '/ lançamento',
      features: [
        { text: 'Implantação em LEO', included: true },
        { text: 'Telemetria Padrão', included: true },
        { text: 'Acoplagem Prioritária', included: false },
      ],
      buttonText: 'Iniciar',
      popular: false,
    },
    {
      name: 'Orbital',
      price: '$8.9M',
      period: '/ lançamento',
      features: [
        { text: 'Implantação em MEO e GEO', included: true },
        { text: 'Link de Telemetria Quântica', included: true },
        { text: 'Acoplagem Prioritária na ISS', included: true },
      ],
      buttonText: 'Reservar Manifesto',
      popular: true,
    },
    {
      name: 'Espaço Profundo Personalizado',
      price: 'Personalizado',
      period: '',
      features: [
        { text: 'Lunar e Interplanetário', included: true },
        { text: 'Operações de Propulsão Nuclear', included: true },
        { text: 'Controle de Missão Dedicado', included: true },
      ],
      buttonText: 'Contatar Comando',
      popular: false,
    },
  ];

  return (
    <section id="pricing" className="py-32 px-margin-mobile md:px-margin-desktop relative z-10">
      {/* Atmospheric glow behind pricing */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[500px] bg-primary/5 blur-[120px] rounded-full pointer-events-none"></div>
      
      <div className="max-w-container-max mx-auto relative">
        <div className="text-center mb-16 space-y-4">
          <h2 className="font-headline-lg text-headline-lg text-on-surface">Parâmetros de Missão</h2>
          <p className="font-body-md text-body-md text-tertiary max-w-2xl mx-auto">
            Selecione o nível operacional que se alinha aos seus requisitos de implantação orbital.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 items-center">
          {tiers.map((tier, idx) => (
            <div 
              key={idx} 
              className={`glass-panel rounded-2xl p-8 h-fit ${
                tier.popular 
                  ? 'p-10 transform md:-translate-y-4 border-primary/50 relative glow-border-active bg-surface-container/50' 
                  : ''
              }`}
            >
              {tier.popular && (
                <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-1/2 bg-primary-container text-on-primary-container px-4 py-1 rounded-full font-label-caps text-label-caps uppercase tracking-wider text-xs">
                  MAIS UTILIZADO
                </div>
              )}
              
              <h3 className={`font-headline-md text-headline-md text-2xl mb-2 ${tier.popular ? 'text-primary' : 'text-tertiary'}`}>
                {tier.name}
              </h3>
              
              <div className="mb-6">
                <span className="font-display-lg-mobile text-display-lg-mobile text-on-surface">{tier.price}</span>
                {tier.period && (
                  <span className="font-body-md text-body-md text-tertiary"> {tier.period}</span>
                )}
              </div>
              
              <ul className="space-y-4 mb-8 font-body-md text-body-md">
                {tier.features.map((feat, fidx) => (
                  <li 
                    key={fidx} 
                    className={`flex items-center gap-3 ${
                      feat.included ? 'text-on-surface' : 'text-surface-variant'
                    }`}
                  >
                    <span className={`material-symbols-outlined text-sm ${
                      feat.included 
                        ? (tier.popular ? 'text-primary' : 'text-secondary') 
                        : 'text-surface-variant'
                    }`}>
                      {feat.included ? 'check' : 'close'}
                    </span>
                    {feat.text}
                  </li>
                ))}
              </ul>
              
              <button 
                className={`w-full py-4 rounded font-mono-label text-mono-label transition-colors duration-200 ${
                  tier.popular 
                    ? 'bg-primary-container text-on-primary-container hover:bg-primary neon-button-glow' 
                    : 'border border-outline text-on-surface hover:bg-surface-bright'
                }`}
              >
                {tier.buttonText}
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

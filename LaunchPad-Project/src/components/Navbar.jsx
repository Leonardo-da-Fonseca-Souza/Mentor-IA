import React, { useState } from 'react';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <header className="w-full fixed top-0 z-50 bg-background/80 backdrop-blur-md border-b border-white/10 shadow-2xl shadow-primary/20">
      <div className="flex justify-between items-center px-margin-mobile md:px-margin-desktop py-4 max-w-container-max mx-auto">
        <div className="font-display-lg-mobile md:font-headline-md text-headline-md tracking-tighter text-primary">
          LaunchPad
        </div>
        
        <nav className="hidden md:flex gap-8">
          <a className="text-primary font-bold border-b-2 border-primary pb-1" href="#missions">Missões</a>
          <a className="text-on-surface/70 hover:text-primary transition-colors hover:scale-105 duration-200" href="#tech">Tecnologia</a>
          <a className="text-on-surface/70 hover:text-primary transition-colors hover:scale-105 duration-200" href="#payloads">Cargas Úteis</a>
          <a className="text-on-surface/70 hover:text-primary transition-colors hover:scale-105 duration-200" href="#pricing">Preços</a>
        </nav>
        
        <button className="hidden md:block bg-primary-container text-on-primary-container px-6 py-2 rounded font-mono-label hover:opacity-80 scale-95 transition-all neon-button-glow">
          Começar
        </button>

        {/* Mobile Menu Toggle */}
        <button className="md:hidden text-primary" onClick={() => setIsOpen(!isOpen)}>
          <span className="material-symbols-outlined">{isOpen ? 'close' : 'menu'}</span>
        </button>
      </div>

      {/* Mobile Drawer */}
      {isOpen && (
        <div className="md:hidden bg-background/95 border-b border-white/10 px-margin-mobile py-6 space-y-4 flex flex-col backdrop-blur-md">
          <a 
            className="text-primary font-bold py-2 border-b border-white/5" 
            href="#missions"
            onClick={() => setIsOpen(false)}
          >
            Missões
          </a>
          <a 
            className="text-on-surface/70 hover:text-primary transition-colors py-2 border-b border-white/5" 
            href="#tech"
            onClick={() => setIsOpen(false)}
          >
            Tecnologia
          </a>
          <a 
            className="text-on-surface/70 hover:text-primary transition-colors py-2 border-b border-white/5" 
            href="#payloads"
            onClick={() => setIsOpen(false)}
          >
            Cargas Úteis
          </a>
          <a 
            className="text-on-surface/70 hover:text-primary transition-colors py-2 border-b border-white/5" 
            href="#pricing"
            onClick={() => setIsOpen(false)}
          >
            Preços
          </a>
          <button className="w-full bg-primary-container text-on-primary-container py-3 rounded font-mono-label hover:opacity-90 neon-button-glow">
            Começar
          </button>
        </div>
      )}
    </header>
  );
}

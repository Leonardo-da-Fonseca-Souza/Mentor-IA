import React from 'react';

export default function Footer() {
  return (
    <footer className="w-full mt-auto bg-surface-container-lowest border-t border-white/5">
      <div className="flex flex-col md:flex-row justify-between items-center gap-gutter px-margin-mobile md:px-margin-desktop py-12 max-w-container-max mx-auto">
        <div className="font-display-lg-mobile md:font-headline-md text-headline-md text-primary mb-6 md:mb-0">
          LaunchPad
        </div>
        
        <nav className="flex flex-wrap justify-center gap-6 mb-6 md:mb-0">
          <a className="text-on-surface-variant hover:text-secondary transition-colors focus:ring-2 focus:ring-primary outline-none font-body-md text-body-md" href="#">
            Política de Privacidade
          </a>
          <a className="text-on-surface-variant hover:text-secondary transition-colors focus:ring-2 focus:ring-primary outline-none font-body-md text-body-md" href="#">
            Termos de Serviço
          </a>
          <a className="text-on-surface-variant hover:text-secondary transition-colors focus:ring-2 focus:ring-primary outline-none font-body-md text-body-md" href="#">
            Status da Telemetria
          </a>
          <a className="text-on-surface-variant hover:text-secondary transition-colors focus:ring-2 focus:ring-primary outline-none font-body-md text-body-md" href="#">
            Contato
          </a>
        </nav>
        
        <div className="text-secondary font-body-md text-body-md">
          © 2026 LaunchPad Aerospace. Todos os direitos reservados.
        </div>
      </div>
    </footer>
  );
}

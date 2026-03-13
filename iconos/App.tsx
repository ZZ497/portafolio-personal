import React from 'react';
import Hero from './components/Hero';
import Experience from './components/Experience';
import Skills from './components/Skills';
import Projects from './components/Projects';
import ChatWidget from './components/ChatWidget';
import Footer from './components/Footer';

function App() {
  return (
    <div className="min-h-screen bg-slate-50 selection:bg-blue-100 selection:text-blue-900">
      {/* Navigation - Simple Sticky Header */}
      <nav className="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-slate-100 no-print">
        <div className="max-w-6xl mx-auto px-6 h-16 flex items-center justify-between">
          <span className="font-bold text-xl text-slate-900">JP.</span>
          <div className="hidden md:flex gap-8 text-sm font-medium text-slate-600">
            <a href="#" className="hover:text-blue-600 transition-colors">Inicio</a>
            <a href="#experience" className="hover:text-blue-600 transition-colors">Experiencia</a>
            <a href="#skills" className="hover:text-blue-600 transition-colors">Habilidades</a>
            <a href="#projects" className="hover:text-blue-600 transition-colors">Proyectos</a>
          </div>
        </div>
      </nav>

      <main>
        <Hero />
        <Experience />
        <Skills />
        <Projects />
      </main>

      <ChatWidget />
      <Footer />
    </div>
  );
}

export default App;
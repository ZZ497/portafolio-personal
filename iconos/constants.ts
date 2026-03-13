import { ResumeData } from './types';

export const RESUME_DATA: ResumeData = {
  name: "Diego Lijarcio Merino",
  title: "Ingeniero de Software Senior",
  summary: "Desarrollador Full Stack con más de 8 años de experiencia especializándome en tecnologías web modernas. Apasionado por crear experiencias de usuario fluidas, arquitecturas escalables y soluciones impulsadas por IA. Experto en liderar equipos técnicos y en la entrega continua de productos de alto impacto.",
  email: "hola@juanperez.dev",
  phone: "+34 600 123 456",
  location: "Madrid, España",
  social: {
    linkedin: "https://linkedin.com/in/juanperez-demo",
    github: "https://github.com/juanperez-demo",
    twitter: "https://twitter.com/juanperez-demo",
  },
  experience: [
    {
      id: "exp-1",
      role: "Senior Frontend Engineer",
      company: "TechSolutions Global",
      period: "2021 - Presente",
      description: "Liderando el equipo de frontend para la plataforma principal SaaS.",
      achievements: [
        "Reduje el tiempo de carga de la aplicación en un 40% migrando a Next.js.",
        "Implementé un sistema de diseño (Design System) utilizado por 5 equipos diferentes.",
        "Mentoricé a 3 desarrolladores junior hasta alcanzar el nivel senior."
      ]
    },
    {
      id: "exp-2",
      role: "Full Stack Developer",
      company: "Innovate StartUp",
      period: "2018 - 2021",
      description: "Desarrollo integral de aplicaciones web para clientes fintech.",
      achievements: [
        "Desarrollé una pasarela de pagos segura procesando >$1M mensuales.",
        "Integré servicios de IA para detección de fraude en tiempo real.",
        "Optimicé las consultas de base de datos reduciendo costos de AWS en un 25%."
      ]
    },
    {
      id: "exp-3",
      role: "Junior Web Developer",
      company: "Agencia Creativa Digital",
      period: "2016 - 2018",
      description: "Creación de sitios web interactivos para campañas de marketing.",
      achievements: [
        "Colaboré en campañas premiadas para marcas internacionales.",
        "Implementé animaciones complejas usando GSAP y WebGL."
      ]
    }
  ],
  education: [
    {
      id: "edu-1",
      degree: "Grado en Ingeniería Informática",
      institution: "Universidad Politécnica de Madrid",
      year: "2012 - 2016"
    },
    {
      id: "edu-2",
      degree: "Máster en Inteligencia Artificial",
      institution: "Tech University Online",
      year: "2019 - 2020"
    }
  ],
  skills: [
    { name: "React / Next.js", level: 95, category: "Frontend" },
    { name: "TypeScript", level: 90, category: "Frontend" },
    { name: "Tailwind CSS", level: 95, category: "Frontend" },
    { name: "Node.js", level: 85, category: "Backend" },
    { name: "PostgreSQL", level: 80, category: "Backend" },
    { name: "Google Cloud / AWS", level: 75, category: "Tools" },
    { name: "Git / CI/CD", level: 85, category: "Tools" },
    { name: "Liderazgo de Equipos", level: 80, category: "Soft Skills" },
  ],
  projects: [
    {
      id: "proj-1",
      title: "E-commerce Dashboard",
      description: "Un panel de administración completo para tiendas online con análisis de datos en tiempo real y gestión de inventario.",
      techStack: ["React", "TypeScript", "Recharts", "Supabase"],
      imageUrl: "https://picsum.photos/600/400?random=1"
    },
    {
      id: "proj-2",
      title: "AI Chat Assistant",
      description: "Widget de chat integrable que utiliza modelos de lenguaje grandes para soporte al cliente automatizado.",
      techStack: ["Node.js", "WebSockets", "Gemini API", "Redis"],
      imageUrl: "https://picsum.photos/600/400?random=2"
    },
    {
      id: "proj-3",
      title: "Health Tracker App",
      description: "Aplicación móvil progresiva (PWA) para seguimiento de hábitos saludables y visualización de progreso.",
      techStack: ["React Native", "Firebase", "D3.js"],
      imageUrl: "https://picsum.photos/600/400?random=3"
    }
  ]
};
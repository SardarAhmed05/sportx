import React from 'react';

export default function SportXLogo({ className = "w-9 h-9" }) {
  return (
    <svg 
      className={className} 
      viewBox="0 0 48 48" 
      fill="none" 
      xmlns="http://www.w3.org/2000/svg"
      aria-label="SportX Logo"
    >
      <defs>
        {/* Deep Obsidian / Titanium Gradient */}
        <linearGradient id="sxObsidianComp" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#0F172A"/>
          <stop offset="60%" stopColor="#090D16"/>
          <stop offset="100%" stopColor="#020617"/>
        </linearGradient>

        {/* Championship Emerald Luxury Gradient */}
        <linearGradient id="sxEmeraldComp" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#34D399"/>
          <stop offset="50%" stopColor="#10B981"/>
          <stop offset="100%" stopColor="#059669"/>
        </linearGradient>

        {/* Outer Chamfer Border Glow */}
        <linearGradient id="sxBorderComp" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#34D399" stopOpacity="0.85"/>
          <stop offset="50%" stopColor="#10B981" stopOpacity="0.3"/>
          <stop offset="100%" stopColor="#059669" stopOpacity="0.75"/>
        </linearGradient>

        {/* Platinum Highlight */}
        <linearGradient id="sxPlatinumComp" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#FFFFFF"/>
          <stop offset="100%" stopColor="#E2E8F0"/>
        </linearGradient>
      </defs>

      {/* Luxury Stadium Squircle Base */}
      <rect width="48" height="48" rx="13" fill="url(#sxObsidianComp)"/>
      <rect x="0.75" y="0.75" width="46.5" height="46.5" rx="12.25" stroke="url(#sxBorderComp)" strokeWidth="1.3"/>

      {/* Minimal Classic Monogram: S + X Integrated Insignia */}
      {/* 1. The Dynamic S-Ribbon (Pure Platinum White) */}
      <path 
        d="M 33 13 C 33 13, 20 12, 16 18 C 12.5 23.5, 17 27, 24 28 C 31 29, 35.5 32.5, 32 38 C 28 44, 15 43, 15 43" 
        stroke="url(#sxPlatinumComp)" 
        strokeWidth="4.2" 
        strokeLinecap="round" 
        strokeLinejoin="round"
      />

      {/* 2. The Velocity Cross-Blade (Championship Emerald) forming the 'X' */}
      <path 
        d="M 15 35 L 33 13" 
        stroke="url(#sxEmeraldComp)" 
        strokeWidth="4.2" 
        strokeLinecap="round"
      />

      {/* 3. Center Zenith Spark */}
      <circle cx="24" cy="24" r="1.75" fill="#34D399"/>
    </svg>
  );
}

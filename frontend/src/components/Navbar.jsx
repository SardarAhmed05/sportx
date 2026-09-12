import React, { useState, useEffect, useRef } from 'react';
import { 
  Tv, 
  Search, 
  RefreshCw, 
  Plus, 
  Star, 
  X, 
  Sun, 
  Moon,
  Trophy,
  CircleDot,
  Shield,
  Gauge,
  Crosshair,
  Swords,
  Target,
  ChevronDown,
  Check,
  SlidersHorizontal,
  MessageSquare
} from 'lucide-react';
import SportXLogo from './SportXLogo';

// Pure Lucide-spec SVG icon for Cricket (Bat & Ball, 24x24 grid, 2px stroke, zero emojis)
export const CricketIcon = ({ className = "w-4 h-4" }) => (
  <svg 
    className={className} 
    viewBox="0 0 24 24" 
    fill="none" 
    stroke="currentColor" 
    strokeWidth="2" 
    strokeLinecap="round" 
    strokeLinejoin="round"
  >
    <path d="M4 20l10-10" />
    <path d="M14 10l2 2" />
    <path d="M6 22l-2-2 10-10 2 2-10 10z" />
    <circle cx="19" cy="5" r="2.5" />
  </svg>
);

// Active sports: Football (Default), Cricket, and Tennis
export const SPORTS_CONFIG = [
  { id: 'football', name: 'Football', shortName: 'Football', subtitle: 'Premier League, UCL, La Liga', icon: Trophy },
  { id: 'cricket', name: 'Cricket', shortName: 'Cricket', subtitle: 'ICC World Cup, IPL, PSL, Tests', icon: CricketIcon },
  { id: 'tennis', name: 'Tennis', shortName: 'Tennis', subtitle: 'ATP & WTA Grand Slams', icon: Crosshair },
];

export default function Navbar({ 
  theme = 'light',
  onToggleTheme,
  activeSport = 'football',
  onSelectSport,
  searchQuery, 
  setSearchQuery, 
  onRefreshScraper, 
  isRefreshing, 
  matchCount = 0,
  liveCount = 0,
  favoritesCount = 0,
  onCustomStreamOpen,
  onOpenFavorites,
  onGoHome
}) {
  const [isSportOpen, setIsSportOpen] = useState(false);
  const [isMobileSearchOpen, setIsMobileSearchOpen] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const sportMenuRef = useRef(null);
  const mobileMenuRef = useRef(null);
  const searchInputRef = useRef(null);

  // Close desktop dropdown on click outside
  useEffect(() => {
    function handleClickOutside(event) {
      if (sportMenuRef.current && !sportMenuRef.current.contains(event.target)) {
        setIsSportOpen(false);
      }
      if (mobileMenuRef.current && !mobileMenuRef.current.contains(event.target)) {
        setIsMobileMenuOpen(false);
      }
    }
    if (isSportOpen || isMobileMenuOpen) {
      document.addEventListener('mousedown', handleClickOutside);
      document.addEventListener('touchstart', handleClickOutside);
    }
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
      document.removeEventListener('touchstart', handleClickOutside);
    };
  }, [isSportOpen, isMobileMenuOpen]);

  // Focus mobile search input when expanded
  useEffect(() => {
    if (isMobileSearchOpen && searchInputRef.current) {
      searchInputRef.current.focus();
    }
  }, [isMobileSearchOpen]);

  const currentSport = SPORTS_CONFIG.find(s => s.id === activeSport) || SPORTS_CONFIG[0];
  const ActiveSportIcon = currentSport.icon;

  return (
    <header className="sticky top-0 z-40 bg-white/95 dark:bg-slate-900/95 backdrop-blur-md border-b border-slate-200/90 dark:border-slate-800 shadow-xs transition-colors duration-200">
      <div className="max-w-7xl mx-auto px-3 sm:px-6 lg:px-8 h-16 flex items-center justify-between relative">
        
        {/* ============================================================ */}
        {/* LEFT SECTION: Minimal Classic Brand Logo                     */}
        {/* ============================================================ */}
        <div className="flex items-center gap-2 sm:gap-3 shrink-0 z-10">
          {/* Brand Logo (Clickable -> Returns to Home Page) */}
          <button 
            onClick={onGoHome}
            className="flex items-center gap-2 sm:gap-2.5 select-none cursor-pointer group text-left bg-transparent border-0 p-0 focus:outline-hidden"
            title="Return to SportX Home"
            aria-label="Return to SportX Home"
          >
            <div className="group-hover:scale-105 transition-transform duration-200 drop-shadow-md">
              <SportXLogo className="w-8 h-8 sm:w-9 sm:h-9" />
            </div>
            <div className="flex flex-col">
              <span className="text-base sm:text-lg font-black tracking-tight text-slate-900 dark:text-white leading-none">
                SPORT<span className="text-emerald-500">X</span>
              </span>
              <span className="text-[8px] sm:text-[9px] font-extrabold text-slate-400 dark:text-slate-500 tracking-[0.15em] uppercase mt-0.5">
                Sports Hub
              </span>
            </div>
          </button>
        </div>

        {/* ============================================================ */}
        {/* CENTER SECTION: 100% MATHEMATICALLY DEAD-CENTER DROPDOWN      */}
        {/* Uses absolute left-1/2 -translate-x-1/2 to guarantee true     */}
        {/* geometric center unaffected by left or right item widths     */}
        {/* ============================================================ */}
        <div className="hidden md:flex absolute left-1/2 -translate-x-1/2 top-1/2 -translate-y-1/2 items-center justify-center z-30 pointer-events-auto">
          <div className="relative" ref={sportMenuRef}>
            <button
              onClick={() => setIsSportOpen(!isSportOpen)}
              className="flex items-center gap-2 px-4 py-2 rounded-xl bg-emerald-500/10 hover:bg-emerald-500/20 dark:bg-emerald-950/70 dark:hover:bg-emerald-900/80 text-emerald-900 dark:text-emerald-200 text-xs font-black border border-emerald-500/30 dark:border-emerald-700/60 shadow-2xs hover:shadow-xs transition-all cursor-pointer select-none"
              title="Switch Sport (Football, Cricket, Tennis)"
            >
              <ActiveSportIcon className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0" />
              <span className="font-black tracking-tight">{currentSport.name}</span>
              <ChevronDown className={`w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 transition-transform duration-200 ${isSportOpen ? 'rotate-180' : ''}`} />
            </button>

            {isSportOpen && (
              <div className="absolute left-1/2 -translate-x-1/2 mt-2 w-64 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-1.5 z-50 animate-in fade-in zoom-in-95 duration-150">
                <div className="px-2.5 py-1 text-[10px] font-black uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  Switch Sport
                </div>
                <div className="space-y-1 mt-1 max-h-80 overflow-y-auto scrollbar-none">
                  {SPORTS_CONFIG.map((sp) => {
                    const Icon = sp.icon;
                    const isActive = sp.id === activeSport;
                    return (
                      <button
                        key={sp.id}
                        onClick={() => {
                          if (onSelectSport) onSelectSport(sp.id);
                          setIsSportOpen(false);
                        }}
                        className={`w-full flex items-center justify-between px-2.5 py-2 rounded-xl text-xs font-bold transition-all cursor-pointer ${
                          isActive
                            ? 'bg-emerald-600 text-white shadow-xs'
                            : 'text-slate-700 dark:text-slate-300 hover:bg-slate-100 dark:hover:bg-slate-800'
                        }`}
                      >
                        <div className="flex items-center gap-2.5">
                          <div className={`w-7 h-7 rounded-lg flex items-center justify-center shrink-0 ${
                            isActive ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400'
                          }`}>
                            <Icon className="w-3.5 h-3.5" />
                          </div>
                          <div className="text-left">
                            <div className="font-bold leading-tight">{sp.name}</div>
                            <div className={`text-[10px] ${isActive ? 'text-emerald-100' : 'text-slate-400'}`}>{sp.subtitle}</div>
                          </div>
                        </div>
                        {isActive && <Check className="w-3.5 h-3.5 text-white shrink-0 ml-2" />}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        </div>

        {/* ============================================================ */}
        {/* MOBILE CENTER: Compact Sport Pill for mobile touch           */}
        {/* ============================================================ */}
        <div className="flex md:hidden items-center justify-center z-10">
          <button
            onClick={() => setIsSportOpen(true)}
            className="flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-emerald-500/10 dark:bg-emerald-950/70 border border-emerald-500/30 dark:border-emerald-700/60 text-emerald-900 dark:text-emerald-200 text-xs font-black shadow-2xs active:scale-95 transition-all cursor-pointer"
          >
            <ActiveSportIcon className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
            <span className="truncate max-w-[80px]">{currentSport.shortName || currentSport.name}</span>
            <ChevronDown className="w-3 h-3 text-emerald-600 dark:text-emerald-400" />
          </button>
        </div>

        {/* ============================================================ */}
        {/* RIGHT SECTION: Desktop Actions Cluster & Mobile Icon Bar     */}
        {/* ============================================================ */}
        <div className="flex items-center gap-1.5 sm:gap-2 shrink-0 justify-end z-10">

          {/* Desktop Actions Cluster (Feedback, Saved, Custom URL, Theme Toggle, Refresh) */}
          <div className="hidden md:flex items-center gap-1.5 lg:gap-2">
            {/* 1. Drop Community Feedback Button */}
            <button
              onClick={() => {
                const el = document.getElementById('feedback-section');
                if (el) el.scrollIntoView({ behavior: 'smooth' });
              }}
              className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-emerald-50 hover:bg-emerald-100 dark:bg-emerald-950/50 dark:hover:bg-emerald-900/60 text-emerald-700 dark:text-emerald-300 border border-emerald-200 dark:border-emerald-800 text-xs font-bold transition-all cursor-pointer whitespace-nowrap shadow-2xs"
              title="Drop Community Feedback & Stream Requests"
            >
              <MessageSquare className="w-3.5 h-3.5 text-emerald-600 dark:text-emerald-400 shrink-0" />
              <span className="text-[11px] hidden xl:inline">Feedback</span>
            </button>

            {/* 2. Saved Favorites Button */}
            <button
              onClick={onOpenFavorites}
              className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-rose-50 hover:bg-rose-100 dark:bg-rose-950/40 dark:hover:bg-rose-900/60 text-rose-700 dark:text-rose-300 border border-rose-200 dark:border-rose-900/60 text-xs font-bold transition-all cursor-pointer whitespace-nowrap shadow-2xs"
              title="View Saved Favorites"
            >
              <Star className="w-3.5 h-3.5 fill-rose-600 text-rose-600 dark:fill-rose-400 dark:text-rose-400 shrink-0" />
              <span className="text-[11px] hidden xl:inline">Saved</span>
              <span className="px-1.5 py-0.2 rounded-full bg-rose-200 dark:bg-rose-900/80 text-rose-800 dark:text-rose-200 text-[10px] font-black">
                {favoritesCount}
              </span>
            </button>

            {/* 3. Desktop Search Toggle (icon only, expands drawer below) */}
            <button
              onClick={() => setIsMobileSearchOpen(!isMobileSearchOpen)}
              className={`p-2 rounded-xl border transition-all cursor-pointer ${
                isMobileSearchOpen || searchQuery
                  ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-600 dark:text-emerald-400'
                  : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
              }`}
              aria-label="Toggle Search"
              title="Search matches and teams"
            >
              <Search className="w-4 h-4" />
            </button>

            {/* 4. Custom Stream URL Button */}
            <button
              onClick={onCustomStreamOpen}
              className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition-colors cursor-pointer"
              title="Play Custom Stream URL"
              aria-label="Play Custom Stream URL"
            >
              <Plus className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
            </button>

            {/* 5. Light / Dark Theme Toggle Button */}
            <button
              onClick={onToggleTheme}
              className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-200 border border-slate-200 dark:border-slate-700 transition-all cursor-pointer select-none"
              title={theme === 'dark' ? "Switch to Light Theme" : "Switch to Dark Theme"}
              aria-label="Toggle light and dark theme"
            >
              {theme === 'dark' ? (
                <Sun className="w-4 h-4 text-amber-400 fill-amber-400" />
              ) : (
                <Moon className="w-4 h-4 text-slate-700 fill-slate-700" />
              )}
            </button>

            {/* 6. Desktop Scraper Refresh */}
            <button
              onClick={onRefreshScraper}
              disabled={isRefreshing}
              className="p-2 rounded-xl bg-slate-100 hover:bg-slate-200 dark:bg-slate-800 dark:hover:bg-slate-750 text-slate-700 dark:text-slate-300 border border-slate-200 dark:border-slate-700 transition-all cursor-pointer disabled:opacity-50"
              title="Refresh Feeds"
              aria-label="Refresh Feeds"
            >
              <RefreshCw className={`w-4 h-4 ${isRefreshing ? 'animate-spin text-emerald-600 dark:text-emerald-400' : ''}`} />
            </button>
          </div>

          {/* ---------------- MOBILE ACTION ICONS (Uncluttered) ---------------- */}
          {/* 1. Mobile Search Toggle Icon */}
          <button
            onClick={() => setIsMobileSearchOpen(!isMobileSearchOpen)}
            className={`flex md:hidden p-2 rounded-xl border transition-all cursor-pointer ${
              isMobileSearchOpen || searchQuery
                ? 'bg-emerald-500/15 border-emerald-500/40 text-emerald-600 dark:text-emerald-400'
                : 'bg-slate-100 dark:bg-slate-800 border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300'
            }`}
            aria-label="Toggle Search"
          >
            <Search className="w-4 h-4" />
          </button>

          {/* 2. Mobile Saved Favorites Icon with Badge */}
          <button
            onClick={onOpenFavorites}
            className="relative flex md:hidden p-2 rounded-xl bg-rose-50 dark:bg-rose-950/40 border border-rose-200 dark:border-rose-900/60 text-rose-700 dark:text-rose-300 transition-all cursor-pointer"
            aria-label="View Saved Favorites"
          >
            <Star className="w-4 h-4 fill-rose-600 text-rose-600 dark:fill-rose-400 dark:text-rose-400" />
            {favoritesCount > 0 && (
              <span className="absolute -top-1 -right-1 w-4 h-4 rounded-full bg-rose-600 text-white text-[9px] font-black flex items-center justify-center shadow-xs">
                {favoritesCount}
              </span>
            )}
          </button>

          {/* 3. Mobile Settings / Menu Toggle (Theme, Custom URL, Refresh) */}
          <div className="relative md:hidden" ref={mobileMenuRef}>
            <button
              onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
              className="p-2 rounded-xl bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 transition-all cursor-pointer"
              aria-label="More Options"
            >
              <SlidersHorizontal className="w-4 h-4" />
            </button>

            {/* Mobile Dropdown Menu Popover */}
            {isMobileMenuOpen && (
              <div className="absolute right-0 mt-2 w-52 bg-white dark:bg-slate-900 rounded-2xl shadow-2xl border border-slate-200 dark:border-slate-800 p-2 z-50 animate-in fade-in zoom-in-95 duration-150 space-y-1">
                <div className="px-2.5 py-1 text-[10px] font-black uppercase tracking-wider text-slate-400 dark:text-slate-500">
                  Quick Controls
                </div>

                {/* Theme Toggle */}
                <button
                  onClick={() => {
                    onToggleTheme();
                    setIsMobileMenuOpen(false);
                  }}
                  className="w-full flex items-center justify-between px-2.5 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
                >
                  <span className="flex items-center gap-2">
                    {theme === 'dark' ? <Sun className="w-4 h-4 text-amber-400 fill-amber-400" /> : <Moon className="w-4 h-4 text-slate-700 fill-slate-700" />}
                    <span>{theme === 'dark' ? 'Light Theme' : 'Dark Theme'}</span>
                  </span>
                  <span className="text-[10px] font-bold text-slate-400 uppercase">{theme}</span>
                </button>

                {/* Custom URL */}
                <button
                  onClick={() => {
                    onCustomStreamOpen();
                    setIsMobileMenuOpen(false);
                  }}
                  className="w-full flex items-center gap-2 px-2.5 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
                >
                  <Plus className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                  <span>Custom Stream URL</span>
                </button>

                {/* Drop Feedback */}
                <button
                  onClick={() => {
                    setIsMobileMenuOpen(false);
                    const el = document.getElementById('feedback-section');
                    if (el) el.scrollIntoView({ behavior: 'smooth' });
                  }}
                  className="w-full flex items-center gap-2 px-2.5 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer"
                >
                  <MessageSquare className="w-4 h-4 text-emerald-600 dark:text-emerald-400" />
                  <span>Drop Feedback</span>
                </button>

                {/* Refresh Feeds */}
                <button
                  onClick={() => {
                    onRefreshScraper();
                    setIsMobileMenuOpen(false);
                  }}
                  disabled={isRefreshing}
                  className="w-full flex items-center gap-2 px-2.5 py-2 rounded-xl text-xs font-bold text-slate-700 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800 transition-colors cursor-pointer disabled:opacity-50"
                >
                  <RefreshCw className={`w-4 h-4 text-emerald-600 dark:text-emerald-400 ${isRefreshing ? 'animate-spin' : ''}`} />
                  <span>Refresh All Feeds</span>
                </button>
              </div>
            )}
          </div>

        </div>

      </div>

      {/* ============================================================ */}
      {/* MOBILE EXPANDABLE SEARCH BAR (Clean, spacious, uncluttered)   */}
      {/* ============================================================ */}
      {isMobileSearchOpen && (
        <div className="px-4 pb-3 pt-1 border-t border-slate-100 dark:border-slate-800/80 animate-in slide-in-from-top-2 duration-150">
          <div className="relative flex items-center">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              ref={searchInputRef}
              type="text"
              placeholder="Search matches, teams, leagues..."
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="w-full pl-9 pr-16 py-2 bg-slate-100 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-900 dark:text-slate-100 placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-emerald-500"
            />
            <div className="absolute right-2.5 top-1/2 -translate-y-1/2 flex items-center gap-1.5">
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="text-slate-400 hover:text-slate-600 dark:hover:text-slate-200 p-1 rounded-full cursor-pointer"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              )}
              <button
                onClick={() => {
                  setSearchQuery('');
                  setIsMobileSearchOpen(false);
                }}
                className="text-[11px] font-bold text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white px-1.5 py-0.5 rounded cursor-pointer"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}

      {/* ============================================================ */}
      {/* MOBILE FULL-SCREEN / BOTTOM-SHEET SPORT SELECTOR MODAL       */}
      {/* Native-app feel with large comfortable touch targets          */}
      {/* ============================================================ */}
      {isSportOpen && (
        <div className="md:hidden fixed inset-0 z-50 flex items-end bg-slate-950/60 backdrop-blur-xs animate-in fade-in duration-200">
          <div className="w-full bg-white dark:bg-slate-900 rounded-t-3xl border-t border-slate-200 dark:border-slate-800 p-4 max-h-[85vh] flex flex-col shadow-2xl animate-in slide-in-from-bottom duration-250">
            {/* Handle bar + Header */}
            <div className="flex flex-col items-center pb-3 border-b border-slate-100 dark:border-slate-800">
              <div className="w-10 h-1 rounded-full bg-slate-300 dark:bg-slate-700 mb-3" />
              <div className="w-full flex items-center justify-between">
                <div>
                  <h3 className="text-base font-black text-slate-900 dark:text-white">Select Sport</h3>
                  <p className="text-xs text-slate-500 dark:text-slate-400">Switch live feeds, replays & TV channels</p>
                </div>
                <button
                  onClick={() => setIsSportOpen(false)}
                  className="p-1.5 rounded-full bg-slate-100 dark:bg-slate-800 text-slate-500 dark:text-slate-400 hover:text-slate-800 dark:hover:text-white cursor-pointer"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>
            </div>

            {/* Sports List (Cricket #1 at top) */}
            <div className="overflow-y-auto py-2 space-y-1.5 divide-y divide-slate-100 dark:divide-slate-800/60">
              {SPORTS_CONFIG.map((sp) => {
                const Icon = sp.icon;
                const isActive = sp.id === activeSport;
                return (
                  <button
                    key={sp.id}
                    onClick={() => {
                      if (onSelectSport) onSelectSport(sp.id);
                      setIsSportOpen(false);
                    }}
                    className={`w-full flex items-center justify-between p-3 rounded-2xl transition-all cursor-pointer ${
                      isActive
                        ? 'bg-emerald-600 text-white shadow-md'
                        : 'text-slate-800 dark:text-slate-200 hover:bg-slate-100 dark:hover:bg-slate-800'
                    }`}
                  >
                    <div className="flex items-center gap-3.5">
                      <div className={`w-10 h-10 rounded-xl flex items-center justify-center shrink-0 ${
                        isActive ? 'bg-white/20 text-white' : 'bg-slate-100 dark:bg-slate-800 text-emerald-600 dark:text-emerald-400'
                      }`}>
                        <Icon className="w-5 h-5" />
                      </div>
                      <div className="text-left">
                        <div className="text-sm font-black leading-tight">{sp.name}</div>
                        <div className={`text-xs mt-0.5 ${isActive ? 'text-emerald-100' : 'text-slate-400'}`}>
                          {sp.subtitle}
                        </div>
                      </div>
                    </div>
                    {isActive && <Check className="w-5 h-5 text-white shrink-0 ml-2" />}
                  </button>
                );
              })}
            </div>
          </div>
        </div>
      )}

    </header>
  );
}

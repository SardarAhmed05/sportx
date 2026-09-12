import React, { useState, useEffect } from 'react';
import { 
  MessageSquare, 
  Send, 
  ThumbsUp, 
  Star, 
  CheckCircle2, 
  AlertCircle, 
  Sparkles,
  User,
  Clock
} from 'lucide-react';
import { fetchFeedback, submitFeedback, likeFeedback } from '../services/api';

const CATEGORIES = [
  { id: 'General Feedback', label: 'General' },
  { id: 'Stream Request', label: 'Stream Request' },
  { id: 'Bug Report', label: 'Bug Report' },
  { id: 'Feature Suggestion', label: 'Feature Suggestion' },
];

export default function FeedbackSection() {
  const [comments, setComments] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [successMessage, setSuccessMessage] = useState('');
  const [errorMessage, setErrorMessage] = useState('');

  // Form State
  const [userName, setUserName] = useState(() => {
    try {
      return localStorage.getItem('sportx_user_name') || '';
    } catch {
      return '';
    }
  });
  const [category, setCategory] = useState('General Feedback');
  const [rating, setRating] = useState(5);
  const [commentText, setCommentText] = useState('');
  const [likedIds, setLikedIds] = useState(new Set());

  // Load comments on mount
  useEffect(() => {
    let mounted = true;
    setIsLoading(true);
    fetchFeedback()
      .then((data) => {
        if (mounted && Array.isArray(data)) {
          setComments(data);
        }
      })
      .catch((err) => {
        console.warn('Failed to load feedback:', err);
      })
      .finally(() => {
        if (mounted) setIsLoading(false);
      });

    return () => {
      mounted = false;
    };
  }, []);

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!commentText.trim()) return;

    setIsSubmitting(true);
    setErrorMessage('');
    setSuccessMessage('');

    const trimmedUser = userName.trim() || 'Anonymous Fan';
    try {
      localStorage.setItem('sportx_user_name', trimmedUser);
    } catch (e) {}

    try {
      const newEntry = await submitFeedback({
        user_name: trimmedUser,
        category,
        rating,
        comment: commentText.trim()
      });

      setComments((prev) => [newEntry, ...prev]);
      setCommentText('');
      setSuccessMessage('Thank you! Your feedback has been posted.');
      setTimeout(() => setSuccessMessage(''), 4000);
    } catch (err) {
      setErrorMessage('Could not submit feedback. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleLike = async (id) => {
    if (likedIds.has(id)) return;

    setLikedIds((prev) => new Set(prev).add(id));
    setComments((prev) =>
      prev.map((c) => (c.id === id ? { ...c, likes: (c.likes || 0) + 1 } : c))
    );

    try {
      await likeFeedback(id);
    } catch (err) {
      console.warn('Like request failed:', err);
    }
  };

  const getInitials = (name) => {
    const clean = (name || 'U').trim();
    const parts = clean.split(/\s+/);
    if (parts.length >= 2) return (parts[0][0] + parts[1][0]).toUpperCase();
    return clean.slice(0, 2).toUpperCase();
  };

  return (
    <section id="feedback-section" className="scroll-mt-24 pt-6 pb-12 border-t border-slate-200 dark:border-slate-800">
      <div className="max-w-7xl mx-auto space-y-6">
        
        {/* Section Header */}
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-3 border-b border-slate-200 dark:border-slate-800">
          <div>
            <h2 className="text-xl sm:text-2xl font-black text-slate-900 dark:text-white tracking-tight flex items-center gap-2.5">
              <MessageSquare className="w-6 h-6 text-emerald-600 dark:text-emerald-400" />
              <span>Community Hub & Feedback</span>
            </h2>
            <p className="text-xs sm:text-sm text-slate-500 dark:text-slate-400 mt-0.5">
              Request channels, suggest improvements, report stream issues, or share your thoughts with fellow sports fans.
            </p>
          </div>
          <div className="flex items-center gap-2">
            <span className="px-3 py-1 rounded-full bg-emerald-50 dark:bg-emerald-950/50 text-emerald-700 dark:text-emerald-300 text-xs font-bold border border-emerald-200 dark:border-emerald-800">
              {comments.length} Comments
            </span>
          </div>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Form Column (1 col) */}
          <div className="lg:col-span-1">
            <div className="bg-white dark:bg-slate-900 rounded-3xl p-5 border border-slate-200/90 dark:border-slate-800 shadow-sm sticky top-24 space-y-4">
              <div className="flex items-center gap-2">
                <Sparkles className="w-4 h-4 text-emerald-500" />
                <h3 className="text-sm font-extrabold text-slate-900 dark:text-white uppercase tracking-wider">
                  Drop Your Thoughts
                </h3>
              </div>

              {successMessage && (
                <div className="p-3 rounded-2xl bg-emerald-50 dark:bg-emerald-950/50 border border-emerald-200 dark:border-emerald-800 text-emerald-800 dark:text-emerald-300 text-xs font-bold flex items-center gap-2">
                  <CheckCircle2 className="w-4 h-4 text-emerald-600 dark:text-emerald-400 shrink-0" />
                  <span>{successMessage}</span>
                </div>
              )}

              {errorMessage && (
                <div className="p-3 rounded-2xl bg-rose-50 dark:bg-rose-950/50 border border-rose-200 dark:border-rose-800 text-rose-800 dark:text-rose-300 text-xs font-bold flex items-center gap-2">
                  <AlertCircle className="w-4 h-4 text-rose-600 dark:text-rose-400 shrink-0" />
                  <span>{errorMessage}</span>
                </div>
              )}

              <form onSubmit={handleSubmit} className="space-y-3.5">
                {/* Name */}
                <div>
                  <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 mb-1">
                    Your Name / Handle
                  </label>
                  <div className="relative">
                    <User className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
                    <input
                      type="text"
                      placeholder="e.g. Alex (or leave blank for Anonymous)"
                      value={userName}
                      onChange={(e) => setUserName(e.target.value)}
                      maxLength={40}
                      className="w-full pl-9 pr-3 py-2 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-emerald-500"
                    />
                  </div>
                </div>

                {/* Category Selector */}
                <div>
                  <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 mb-1.5">
                    Category
                  </label>
                  <div className="grid grid-cols-2 gap-1.5">
                    {CATEGORIES.map((cat) => (
                      <button
                        type="button"
                        key={cat.id}
                        onClick={() => setCategory(cat.id)}
                        className={`px-2.5 py-1.5 rounded-xl text-xs font-bold transition-all cursor-pointer text-center ${
                          category === cat.id
                            ? 'bg-emerald-600 text-white shadow-xs'
                            : 'bg-slate-50 dark:bg-slate-800 text-slate-600 dark:text-slate-300 border border-slate-200 dark:border-slate-700 hover:bg-slate-100 dark:hover:bg-slate-750'
                        }`}
                      >
                        {cat.label}
                      </button>
                    ))}
                  </div>
                </div>

                {/* Rating */}
                <div>
                  <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 mb-1">
                    Stream & App Rating
                  </label>
                  <div className="flex items-center gap-1">
                    {[1, 2, 3, 4, 5].map((star) => (
                      <button
                        type="button"
                        key={star}
                        onClick={() => setRating(star)}
                        className="p-1 rounded-lg hover:scale-110 transition-transform cursor-pointer"
                        title={`${star} Star${star > 1 ? 's' : ''}`}
                      >
                        <Star
                          className={`w-5 h-5 ${
                            star <= rating
                              ? 'text-amber-400 fill-amber-400'
                              : 'text-slate-300 dark:text-slate-600'
                          }`}
                        />
                      </button>
                    ))}
                    <span className="text-xs font-bold text-slate-500 dark:text-slate-400 ml-2">
                      {rating} of 5
                    </span>
                  </div>
                </div>

                {/* Comment */}
                <div>
                  <label className="block text-[11px] font-bold uppercase tracking-wider text-slate-600 dark:text-slate-400 mb-1">
                    Message / Request
                  </label>
                  <textarea
                    rows={4}
                    required
                    placeholder="Share feedback, match requests, or questions..."
                    value={commentText}
                    onChange={(e) => setCommentText(e.target.value)}
                    maxLength={600}
                    className="w-full p-3 bg-slate-50 dark:bg-slate-800 border border-slate-200 dark:border-slate-700 rounded-2xl text-xs text-slate-900 dark:text-white placeholder:text-slate-400 dark:placeholder:text-slate-500 focus:outline-none focus:border-emerald-500 resize-none"
                  />
                  <div className="text-right text-[10px] text-slate-400 mt-1">
                    {commentText.length}/600
                  </div>
                </div>

                {/* Submit */}
                <button
                  type="submit"
                  disabled={isSubmitting || !commentText.trim()}
                  className="w-full py-3 px-4 rounded-2xl bg-emerald-600 hover:bg-emerald-500 text-white font-black text-xs transition-all shadow-md shadow-emerald-600/20 disabled:opacity-50 disabled:cursor-not-allowed cursor-pointer flex items-center justify-center gap-2"
                >
                  <Send className="w-3.5 h-3.5" />
                  <span>{isSubmitting ? 'Posting...' : 'Post Feedback'}</span>
                </button>
              </form>
            </div>
          </div>

          {/* Comments Feed Column (2 cols) */}
          <div className="lg:col-span-2 space-y-3.5">
            {isLoading ? (
              <div className="py-16 text-center bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800">
                <div className="w-8 h-8 rounded-full border-2 border-emerald-500/20 border-t-emerald-500 animate-spin mx-auto mb-2"></div>
                <p className="text-xs text-slate-500 dark:text-slate-400">Loading community thoughts...</p>
              </div>
            ) : comments.length === 0 ? (
              <div className="py-16 text-center bg-white dark:bg-slate-900 rounded-3xl border border-slate-200 dark:border-slate-800 space-y-2">
                <MessageSquare className="w-8 h-8 text-slate-400 dark:text-slate-600 mx-auto" />
                <h4 className="text-sm font-bold text-slate-800 dark:text-slate-200">No feedback yet</h4>
                <p className="text-xs text-slate-500 dark:text-slate-400">Be the first to share your thoughts or stream request!</p>
              </div>
            ) : (
              comments.map((item) => {
                const isLiked = likedIds.has(item.id);
                return (
                  <div
                    key={item.id}
                    className="bg-white dark:bg-slate-900 rounded-2xl p-4 sm:p-5 border border-slate-200/90 dark:border-slate-800 hover:border-slate-300 dark:hover:border-slate-700 transition-colors space-y-2.5 shadow-2xs"
                  >
                    {/* Comment Header */}
                    <div className="flex items-center justify-between gap-3">
                      <div className="flex items-center gap-3 min-w-0">
                        <div className="w-9 h-9 rounded-xl bg-slate-100 dark:bg-slate-800 text-emerald-600 dark:text-emerald-400 font-extrabold text-xs flex items-center justify-center shrink-0 border border-slate-200 dark:border-slate-700">
                          {getInitials(item.user_name)}
                        </div>
                        <div className="min-w-0">
                          <div className="flex items-center gap-2">
                            <span className="text-xs sm:text-sm font-bold text-slate-900 dark:text-white truncate">
                              {item.user_name || 'Fan'}
                            </span>
                            <span className="px-2 py-0.5 rounded-md bg-slate-100 dark:bg-slate-800 text-slate-600 dark:text-slate-400 text-[10px] font-bold">
                              {item.category || 'Feedback'}
                            </span>
                          </div>
                          <div className="flex items-center gap-1.5 text-[11px] text-slate-400 mt-0.5">
                            <Clock className="w-3 h-3" />
                            <span>{item.created_at || 'Recently'}</span>
                          </div>
                        </div>
                      </div>

                      {/* Stars */}
                      <div className="flex items-center gap-0.5 shrink-0">
                        {[1, 2, 3, 4, 5].map((s) => (
                          <Star
                            key={s}
                            className={`w-3.5 h-3.5 ${
                              s <= (item.rating || 5)
                                ? 'text-amber-400 fill-amber-400'
                                : 'text-slate-200 dark:text-slate-700'
                            }`}
                          />
                        ))}
                      </div>
                    </div>

                    {/* Comment Text */}
                    <p className="text-xs sm:text-sm text-slate-700 dark:text-slate-300 leading-relaxed break-words whitespace-pre-wrap">
                      {item.comment}
                    </p>

                    {/* Footer / Like Button */}
                    <div className="pt-2 border-t border-slate-100 dark:border-slate-800/80 flex items-center justify-between">
                      <button
                        onClick={() => handleLike(item.id)}
                        className={`flex items-center gap-1.5 text-xs font-bold px-2.5 py-1 rounded-lg transition-colors cursor-pointer ${
                          isLiked
                            ? 'bg-emerald-50 dark:bg-emerald-950/60 text-emerald-600 dark:text-emerald-400'
                            : 'text-slate-500 hover:text-slate-900 dark:text-slate-400 dark:hover:text-white hover:bg-slate-100 dark:hover:bg-slate-800'
                        }`}
                        title="Like this comment"
                      >
                        <ThumbsUp className={`w-3.5 h-3.5 ${isLiked ? 'fill-emerald-500' : ''}`} />
                        <span>{item.likes || 0} Helpful</span>
                      </button>

                      <span className="text-[10px] text-slate-400 uppercase font-bold tracking-wider">
                        Verified Fan
                      </span>
                    </div>
                  </div>
                );
              })
            )}
          </div>

        </div>

      </div>
    </section>
  );
}

import { useState } from "react";
import SearchBar from "@/components/SearchBar";
import SearchFilters, { FilterType } from "@/components/SearchFilters";
import ResultCard, { SearchResult } from "@/components/ResultCard";
import LoadingSpinner from "@/components/LoadingSpinner";
import EmptyState from "@/components/EmptyState";
import { AnimatePresence } from "framer-motion";

// Mock data generator - ready to be replaced with real API calls
const generateMockResults = (query: string, filter: FilterType): SearchResult[] => {
  const allResults: SearchResult[] = [
    {
      id: "1",
      title: "Understanding React Hooks",
      description: "A comprehensive guide to React Hooks including useState, useEffect, and custom hooks. Learn how to manage state and side effects in functional components.",
      source: "Docs",
      url: "#",
    },
    {
      id: "2",
      title: "TypeScript Best Practices",
      description: "Essential TypeScript patterns and practices for building scalable applications. Covers type safety, generics, and advanced type patterns.",
      source: "GitHub",
      url: "#",
    },
    {
      id: "3",
      title: "Modern CSS Techniques",
      description: "Explore modern CSS features like Grid, Flexbox, and CSS Variables. Learn how to create responsive layouts with minimal code.",
      source: "Articles",
      url: "#",
    },
    {
      id: "4",
      title: "Machine Learning Dataset",
      description: "A curated collection of image classification datasets for training computer vision models. Includes 10,000+ labeled images.",
      source: "Datasets",
      url: "#",
    },
    {
      id: "5",
      title: "API Design Patterns",
      description: "Best practices for designing RESTful APIs. Covers versioning, authentication, rate limiting, and error handling.",
      source: "GitHub",
      url: "#",
    },
    {
      id: "6",
      title: "Natural Language Processing Research",
      description: "Latest research in NLP including transformer models, attention mechanisms, and large language models.",
      source: "arXiv",
      url: "#",
    },
  ];

  if (!query) return [];

  // Filter by type
  let filtered = allResults;
  if (filter !== "all") {
    const sourceMap: Record<FilterType, string[]> = {
      all: [],
      code: ["GitHub", "Docs"],
      articles: ["Articles", "arXiv"],
      datasets: ["Datasets"],
    };
    filtered = allResults.filter((result) =>
      sourceMap[filter]?.includes(result.source)
    );
  }

  // Simple search filter
  return filtered.filter(
    (result) =>
      result.title.toLowerCase().includes(query.toLowerCase()) ||
      result.description.toLowerCase().includes(query.toLowerCase())
  );
};

const Index = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeFilter, setActiveFilter] = useState<FilterType>("all");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;

    setIsLoading(true);
    setHasSearched(true);

    // Simulate API call with delay
    await new Promise((resolve) => setTimeout(resolve, 1500));

    const mockResults = generateMockResults(searchQuery, activeFilter);
    setResults(mockResults);
    setIsLoading(false);
  };

  const handleFilterChange = (filter: FilterType) => {
    setActiveFilter(filter);
    if (hasSearched) {
      const mockResults = generateMockResults(searchQuery, filter);
      setResults(mockResults);
    }
  };

  return (
    <div className="min-h-screen bg-background">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold mb-4 bg-gradient-to-r from-primary to-primary/60 bg-clip-text text-transparent">
            Search Engine
          </h1>
          <p className="text-muted-foreground text-lg">
            Test interface for custom search functionality
          </p>
        </div>

        {/* Search Section */}
        <div className="flex flex-col items-center gap-6 mb-12">
          <SearchBar
            value={searchQuery}
            onChange={setSearchQuery}
            onSearch={handleSearch}
            isLoading={isLoading}
          />
          <SearchFilters
            activeFilter={activeFilter}
            onFilterChange={handleFilterChange}
          />
        </div>

        {/* Results Section */}
        <div className="max-w-5xl mx-auto">
          <AnimatePresence mode="wait">
            {isLoading ? (
              <LoadingSpinner key="loading" />
            ) : hasSearched && results.length === 0 ? (
              <EmptyState key="empty" />
            ) : results.length > 0 ? (
              <div key="results" className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {results.map((result, index) => (
                  <ResultCard key={result.id} result={result} index={index} />
                ))}
              </div>
            ) : (
              <div key="initial" className="text-center py-16">
                <p className="text-muted-foreground">
                  Enter a search query to get started
                </p>
              </div>
            )}
          </AnimatePresence>
        </div>

        {/* API Integration Note */}
        <div className="max-w-5xl mx-auto mt-12 p-6 bg-muted/50 rounded-lg border border-border">
          <h3 className="font-semibold mb-2">Ready for Integration</h3>
          <p className="text-sm text-muted-foreground">
            This interface is modular and ready to connect to your real search API.
            Replace the <code className="bg-background px-2 py-1 rounded">generateMockResults</code> function
            with a call to your backend endpoint like{" "}
            <code className="bg-background px-2 py-1 rounded">/api/search?q=query</code>
          </p>
        </div>
      </div>
    </div>
  );
};

export default Index;

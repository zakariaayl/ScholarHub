import { useState } from "react";
import SearchBar from "@/components/SearchBar";
import SearchFilters, { FilterType } from "@/components/SearchFilters";
import ResultCard, { SearchResult } from "@/components/ResultCard";
import LoadingSpinner from "@/components/LoadingSpinner";
import EmptyState from "@/components/EmptyState";
import FileViewer from "@/components/FileViewer";
import { AnimatePresence } from "framer-motion";

// API Configuration
const API_BASE_URL = "http://localhost:5000/api";

// Backend response interface
interface BackendSearchResult {
  doc_id: number;
  filename: string;
  score: number;
  preview: string;
  metadata?: {
    pays?: string;
    domaine?: string;
  };
}

interface ApiResponse {
  query: string;
  filters: any;
  count: number;
  results: BackendSearchResult[];
}

const Index = () => {
  const [searchQuery, setSearchQuery] = useState("");
  const [activeFilter, setActiveFilter] = useState<FilterType>("all");
  const [results, setResults] = useState<SearchResult[]>([]);
  const [isLoading, setIsLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [selectedFile, setSelectedFile] = useState<BackendSearchResult | null>(null);

  // Convert backend results to frontend SearchResult format
  const convertToSearchResult = (backendResult: BackendSearchResult): SearchResult => {
    return {
      id: backendResult.doc_id.toString(),
      title: backendResult.filename,
      description: backendResult.preview,
      source: backendResult.metadata?.domaine || "Document",
      url: `${API_BASE_URL}/files/${backendResult.filename}`,
      score: backendResult.score,
      metadata: backendResult.metadata,
    };
  };

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;

    setIsLoading(true);
    setHasSearched(true);
    setError(null);

    try {
      // Determine endpoint based on filter
      const endpoint = activeFilter === "datasets" 
        ? "/semantic-search" 
        : "/search";
      
      const response = await fetch(
        `${API_BASE_URL}${endpoint}?q=${encodeURIComponent(searchQuery)}&top_k=10`
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data: ApiResponse = await response.json();
      
      // Convert backend results to frontend format
      const convertedResults = data.results.map(convertToSearchResult);
      setResults(convertedResults);
      
    } catch (err: any) {
      console.error("Search error:", err);
      setError(err.message || "Failed to fetch results. Make sure the backend is running.");
      setResults([]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleFilterChange = (filter: FilterType) => {
    setActiveFilter(filter);
    // Re-run search if user has already searched
    if (hasSearched && searchQuery.trim()) {
      // Small delay to allow state update
      setTimeout(() => {
        handleSearch();
      }, 0);
    }
  };

  const handleOpenFile = (result: SearchResult) => {
    // Convert back to backend format for FileViewer
    const backendResult: BackendSearchResult = {
      doc_id: parseInt(result.id),
      filename: result.title,
      score: result.score || 0,
      preview: result.description,
      metadata: result.metadata,
    };
    setSelectedFile(backendResult);
  };

  const handleCloseFile = () => {
    setSelectedFile(null);
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
            Search through documents using TF-IDF or Semantic search
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
            ) : error ? (
              <div key="error" className="text-center py-16">
                <p className="text-destructive mb-2">Error: {error}</p>
                <p className="text-muted-foreground text-sm">
                  Make sure your Flask backend is running on {API_BASE_URL}
                </p>
              </div>
            ) : hasSearched && results.length === 0 ? (
              <EmptyState key="empty" />
            ) : results.length > 0 ? (
              <div key="results" className="grid grid-cols-1 md:grid-cols-2 gap-6">
                {results.map((result, index) => (
                  <div key={result.id} onClick={() => handleOpenFile(result)}>
                    <ResultCard result={result} index={index} />
                  </div>
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

        {/* API Integration Status */}
        <div className="max-w-5xl mx-auto mt-12 p-6 bg-muted/50 rounded-lg border border-border">
          <h3 className="font-semibold mb-2">Backend Connected</h3>
          <p className="text-sm text-muted-foreground">
            Connected to Flask backend at{" "}
            <code className="bg-background px-2 py-1 rounded">{API_BASE_URL}</code>
          </p>
          {hasSearched && (
            <p className="text-sm text-muted-foreground mt-2">
              Results found: <strong>{results.length}</strong> for query "{searchQuery}"
            </p>
          )}
        </div>
      </div>

      {/* File Viewer Overlay */}
      <AnimatePresence>
        {selectedFile && (
          <FileViewer 
            file={selectedFile} 
            onClose={handleCloseFile}
            apiBaseUrl={API_BASE_URL}
          />
        )}
      </AnimatePresence>
    </div>
  );
};

export default Index;
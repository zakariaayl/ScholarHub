import { motion } from "framer-motion";

export type FilterType = "all" | "code" | "articles" | "datasets";

interface SearchFiltersProps {
  activeFilter: FilterType;
  onFilterChange: (filter: FilterType) => void;
}

const filters: { value: FilterType; label: string; description: string }[] = [
  { value: "all", label: "All", description: "Search all documents" },
  { value: "code", label: "TF-IDF", description: "Traditional keyword matching" },
  { value: "articles", label: "Articles", description: "Article documents" },
  { value: "datasets", label: "Semantic", description: "AI-powered semantic search" },
];

const SearchFilters = ({ activeFilter, onFilterChange }: SearchFiltersProps) => {
  return (
    <div className="flex gap-2 flex-wrap justify-center">
      {filters.map((filter) => (
        <motion.button
          key={filter.value}
          onClick={() => onFilterChange(filter.value)}
          className={`px-4 py-2 rounded-full text-sm font-medium transition-all duration-200 ${
            activeFilter === filter.value
              ? "bg-primary text-primary-foreground shadow-md"
              : "bg-muted text-muted-foreground hover:bg-accent hover:text-accent-foreground"
          }`}
          whileHover={{ scale: 1.05 }}
          whileTap={{ scale: 0.95 }}
          title={filter.description}
        >
          {filter.label}
        </motion.button>
      ))}
    </div>
  );
};

export default SearchFilters;
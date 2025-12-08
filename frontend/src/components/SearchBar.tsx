import { Search } from "lucide-react";
import { Input } from "@/components/ui/input";
import { Button } from "@/components/ui/button";

interface SearchBarProps {
  value: string;
  onChange: (value: string) => void;
  onSearch: () => void;
  isLoading: boolean;
}

const SearchBar = ({ value, onChange, onSearch, isLoading }: SearchBarProps) => {
  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter" && !isLoading) {
      onSearch();
    }
  };

  return (
    <div className="w-full max-w-3xl">
      <div className="relative flex items-center gap-2">
        <div className="relative flex-1">
          <Input
            type="text"
            placeholder="Search documents, scholarships, or keywords…"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            onKeyPress={handleKeyPress}
            className="pr-4 pl-4 py-6 text-lg bg-card border-2 border-border focus:border-primary transition-all duration-200 focus:ring-4 focus:ring-primary/20"
            disabled={isLoading}
          />
        </div>
        <Button
          onClick={onSearch}
          size="lg"
          disabled={isLoading || !value.trim()}
          className="px-6 py-6 bg-primary hover:bg-primary/90 transition-all duration-200 hover:scale-105"
        >
          <Search className="h-5 w-5" />
        </Button>
      </div>
    </div>
  );
};

export default SearchBar;
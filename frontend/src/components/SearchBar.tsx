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
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSearch();
  };

  return (
    <form onSubmit={handleSubmit} className="w-full max-w-3xl">
      <div className="relative flex items-center gap-2">
        <div className="relative flex-1">
          <Input
            type="text"
            placeholder="Search documents, code, or keywords…"
            value={value}
            onChange={(e) => onChange(e.target.value)}
            className="pr-4 pl-4 py-6 text-lg bg-card border-2 border-border focus:border-primary transition-all duration-200 focus:ring-4 focus:ring-primary/20"
            disabled={isLoading}
          />
        </div>
        <Button
          type="submit"
          size="lg"
          disabled={isLoading}
          className="px-6 py-6 bg-primary hover:bg-primary/90 transition-all duration-200 hover:scale-105"
        >
          <Search className="h-5 w-5" />
        </Button>
      </div>
    </form>
  );
};

export default SearchBar;

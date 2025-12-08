import { motion } from "framer-motion";
import { FileText } from "lucide-react";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";

export interface SearchResult {
  id: string;
  title: string;
  description: string;
  source: string;
  url: string;
  score?: number;
  metadata?: {
    pays?: string;
    domaine?: string;
  };
}

interface ResultCardProps {
  result: SearchResult;
  index: number;
}

const ResultCard = ({ result, index }: ResultCardProps) => {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.3, delay: index * 0.1 }}
      className="cursor-pointer"
    >
      <Card className="h-full hover:shadow-lg transition-all duration-200 hover:border-primary/50 bg-card group">
        <CardHeader>
          <div className="flex items-start justify-between gap-2">
            <CardTitle className="text-xl group-hover:text-primary transition-colors duration-200 flex items-center gap-2">
              <FileText className="h-5 w-5 text-primary flex-shrink-0" />
              <span className="truncate">{result.title}</span>
            </CardTitle>
          </div>
          <div className="flex gap-2 flex-wrap items-center">
            <Badge variant="secondary" className="w-fit">
              {result.source}
            </Badge>
            {result.score !== undefined && (
              <Badge variant="outline" className="w-fit">
                Score: {result.score.toFixed(4)}
              </Badge>
            )}
          </div>
        </CardHeader>
        <CardContent>
          <CardDescription className="text-sm leading-relaxed mb-4 line-clamp-3">
            {result.description}
          </CardDescription>
          
          {result.metadata && (
            <div className="flex gap-2 flex-wrap">
              {result.metadata.pays && (
                <Badge variant="outline" className="text-xs">
                  📍 {result.metadata.pays}
                </Badge>
              )}
              {result.metadata.domaine && (
                <Badge variant="outline" className="text-xs">
                  📚 {result.metadata.domaine}
                </Badge>
              )}
            </div>
          )}
        </CardContent>
      </Card>
    </motion.div>
  );
};

export default ResultCard;
import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { FileText, X, Loader2 } from "lucide-react";
import { Badge } from "@/components/ui/badge";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";

interface FileViewerProps {
  file: {
    doc_id: number;
    filename: string;
    score: number;
    preview: string;
    metadata?: {
      pays?: string;
      domaine?: string;
    };
  };
  onClose: () => void;
  apiBaseUrl: string;
}

const FileViewer = ({ file, onClose, apiBaseUrl }: FileViewerProps) => {
  const [fileContent, setFileContent] = useState<string>("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchFile = async () => {
      try {
        setLoading(true);
        setError(null);
        
        const response = await fetch(`${apiBaseUrl}/files/${file.filename}`);
        
        if (!response.ok) {
          throw new Error(`Failed to load file: ${response.status}`);
        }
        
        const text = await response.text();
        setFileContent(text);
      } catch (err: any) {
        console.error("Error loading file:", err);
        setError(err.message || "Failed to load file content");
        setFileContent("");
      } finally {
        setLoading(false);
      }
    };

    fetchFile();
  }, [file.filename, apiBaseUrl]);

  return (
    <>
      {/* Backdrop */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        onClick={onClose}
        className="fixed inset-0 bg-black/50 z-40"
      />

      {/* Viewer Panel */}
      <motion.div
        initial={{ x: "100%" }}
        animate={{ x: 0 }}
        exit={{ x: "100%" }}
        transition={{ type: "spring", damping: 25, stiffness: 200 }}
        className="fixed right-0 top-0 h-full w-full md:w-1/2 bg-background shadow-2xl z-50 overflow-hidden flex flex-col border-l"
      >
        {/* Header */}
        <div className="flex items-center justify-between p-4 border-b bg-muted/50">
          <div className="flex items-center gap-3 flex-1 min-w-0">
            <FileText className="h-5 w-5 text-primary flex-shrink-0" />
            <h2 className="text-lg font-semibold text-foreground truncate">
              {file.filename}
            </h2>
          </div>
          <Button
            onClick={onClose}
            variant="ghost"
            size="icon"
            className="flex-shrink-0"
          >
            <X className="h-5 w-5" />
          </Button>
        </div>

        {/* Metadata */}
        <div className="p-4 border-b bg-muted/30">
          <div className="flex gap-2 flex-wrap items-center">
            <Badge variant="secondary">
              Score: {file.score.toFixed(4)}
            </Badge>
            {file.metadata?.pays && (
              <Badge variant="outline">
                📍 {file.metadata.pays}
              </Badge>
            )}
            {file.metadata?.domaine && (
              <Badge variant="outline">
                📚 {file.metadata.domaine}
              </Badge>
            )}
          </div>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-auto p-6 bg-muted/20">
          {loading ? (
            <div className="flex flex-col items-center justify-center h-full gap-4">
              <Loader2 className="h-8 w-8 text-primary animate-spin" />
              <p className="text-muted-foreground text-sm">Loading file...</p>
            </div>
          ) : error ? (
            <div className="flex flex-col items-center justify-center h-full gap-4">
              <p className="text-destructive">Error: {error}</p>
              <p className="text-muted-foreground text-sm">
                Make sure the file endpoint is configured in your backend
              </p>
            </div>
          ) : (
            <div className="bg-card rounded-lg p-6 shadow-sm border">
              <pre className="text-sm text-foreground whitespace-pre-wrap font-mono leading-relaxed">
                {fileContent}
              </pre>
            </div>
          )}
        </div>
      </motion.div>
    </>
  );
};

export default FileViewer;
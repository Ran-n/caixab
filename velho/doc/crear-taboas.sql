CREATE TABLE "Conta" (
    "IdConta"           TEXT UNIQUE,
    "Nome"              TEXT,
    "Instante Creacion" INTEGER,
    "Descripcion"       TEXT,
    CONSTRAINT contaPK PRIMARY KEY ("IdConta")
);

CREATE TABLE "Divisa" (
    "IdDivisa"                  TEXT UNIQUE,
    "Nome"                      TEXT,
    "Simbolo"                   TEXT,
    "Siglas"                    TEXT,
    "Instante Insercion"        INTEGER,
    "Data Inicio Circulacion"   INTEGER,
    "Tipo"                      String,
    CONSTRAINT divisaPK PRIMARY KEY ("IdDivisa")
);

CREATE TABLE "ValorRelativoDivisa" (
    "IdDivisaAComparar"     TEXT,
    "IdDivisaReferencia"    TEXT,
    "Instante"              INTEGER,
    "ValorUnidade"          FLOAT,
    CONSTRAINT vrdPK PRIMARY KEY ("IdDivisaAComparar", "IdDivisaReferencia"),
    CONSTRAINT vrdFK1 FOREIGN KEY ("IdDivisaAComparar") REFERENCES "Divisa" ("IdDivisa"),
    CONSTRAINT vrdFK2 FOREIGN KEY ("IdDivisaReferencia") REFERENCES "Divisa" ("IdDivisa")    
);

CREATE TABLE "Etiqueta" (
    "IdEtiqueta"        TEXT UNIQUE,
    "Nome"              TEXT,
    "Descripcion"       TEXT,
    "Instante Creacion" TEXT,
    CONSTRAINT etiquetaPK PRIMARY KEY ("IdEtiqueta")
);

CREATE TABLE "Transaccion" (
    "IdTransaccion" TEXT UNIQUE,
    "Identificador" TEXT UNIQUE,
    "Instante"      INTEGER,
    "Cantidade"     TEXT,
    "CantDivisa"    TEXT,
    "De"	        TEXT,
    "Para"		    TEXT,
    "Motivo"	    TEXT,
    "TaxaCant"	    INTEGER,
    "TaxaDivisa"    TEXT,
    "Notas"         TEXT,
    "TipoOperacion" TEXT,
    CONSTRAINT transaccionPK PRIMARY KEY ("IdTransaccion"),
    CONSTRAINT transaccionFK1 FOREIGN KEY ("CantDivisa") REFERENCES "Divisa" ("IdDivisa"),
    CONSTRAINT transacciónFK2 FOREIGN KEY ("TaxaDivisa") REFERENCES "Divisa" ("IdDivisa"),
    CONSTRAINT transacciónFK3 FOREIGN KEY ("De") REFERENCES "Conta" ("IdConta"),
    CONSTRAINT transacciónFK4 FOREIGN KEY ("Para") REFERENCES "Conta" ("IdConta")
);

CREATE TABLE "EtiquetadoTransaccion" (
    "IdEtiqueta"    TEXT,
    "IdTransaccion" TEXT,
    CONSTRAINT etPK PRIMARY KEY ("IdEtiqueta", "IdTransaccion"),
    CONSTRAINT etFK1 FOREIGN KEY ("IdEtiqueta") REFERENCES "Etiqueta" ("IdEtiqueta"),
    CONSTRAINT etFK2 FOREIGN KEY ("IdTransaccion") REFERENCES "Transaccion" ("IdTransaccion")
);

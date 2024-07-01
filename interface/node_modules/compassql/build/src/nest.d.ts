import { SpecQueryModel, SpecQueryModelGroup } from './model';
import { PropIndex } from './propindex';
import { Nest } from './query/groupby';
import { Replacer } from './query/shorthand';
import { SpecQuery } from './query/spec';
import { Dict } from './util';
/**
 * Add a grouping function to the registry.
 */
export declare function registerKeyFn(name: string, keyFn: (specM: SpecQuery) => string): void;
export declare const FIELD = "field";
export declare const FIELD_TRANSFORM = "fieldTransform";
export declare const ENCODING = "encoding";
export declare const SPEC = "spec";
/**
 * Group the input spec query model by a key function registered in the group registry
 * @return
 */
export declare function nest(specModels: SpecQueryModel[], queryNest: Nest[]): SpecQueryModelGroup;
export declare function getGroupByKey(specM: SpecQuery, groupBy: string): string;
export declare const PARSED_GROUP_BY_FIELD_TRANSFORM: {
    include: PropIndex<boolean>;
    replaceIndex: PropIndex<Dict<string>>;
    replacer: PropIndex<Replacer>;
};
export declare const PARSED_GROUP_BY_ENCODING: {
    include: PropIndex<boolean>;
    replaceIndex: PropIndex<Dict<string>>;
    replacer: PropIndex<Replacer>;
};
